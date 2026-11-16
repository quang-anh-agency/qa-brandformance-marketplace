#!/usr/bin/env python3
"""Install only the 13 named agent files; never copy skills or edit config.toml."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import tempfile
import tomllib
import zipfile

PLUGIN = Path(__file__).resolve().parent.parent


def digest(content):
    return hashlib.sha256(content).hexdigest()


def safe_target(path):
    for ancestor in [path, *path.parents]:
        if ancestor.is_symlink():
            raise RuntimeError(f"Refusing symlink target: {ancestor}")


def atomic_write(target, content):
    """Keep the previous file intact if writing the new bytes fails."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".qa-agent-", dir=target.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def plan(agents_root):
    result = []
    for source in sorted((PLUGIN / "assets/agents").glob("*.toml")):
        content = source.read_bytes()
        data = tomllib.loads(content.decode())
        if set(data) != {"name", "description", "developer_instructions"} or source.stem != data["name"]:
            raise RuntimeError(f"Unexpected agent template: {source.name}")
        target = agents_root / source.name
        safe_target(target)
        if target.exists() and not target.is_file():
            raise RuntimeError(f"Target is not a file: {target}")
        old = target.read_bytes() if target.is_file() else None
        state = "unchanged" if old == content else ("new" if old is None else "conflict")
        result.append((target, content, old, state))
    if len(result) != 13:
        raise RuntimeError("Expected exactly 13 QA agent templates")
    return result


def install(agents_root, backup_dir, *, dry_run=False, replace_existing=False, check=False):
    entries = plan(agents_root)
    summary = [{"agent": t.stem, "status": status, "target": str(t)} for t, _, _, status in entries]
    conflicts = [item for item in summary if item["status"] == "conflict"]
    missing = [item for item in summary if item["status"] == "new"]
    if check:
        return {"valid": not conflicts and not missing, "agents": summary}
    if dry_run:
        return {"dry_run": True, "can_install_without_replacement": not conflicts, "agents": summary}
    if conflicts and not replace_existing:
        raise RuntimeError("Existing agents differ; no files written. Review --dry-run before using --replace-existing. Conflicts: " + ", ".join(x["agent"] for x in conflicts))
    changed = [(t, content, old) for t, content, old, state in entries if state != "unchanged"]
    if not changed:
        return {"installed": True, "changed": 0, "verified": 13, "backup": None}
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup = backup_dir / ("qa-agents-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + ".zip")
    records = []
    with zipfile.ZipFile(backup, "x", zipfile.ZIP_DEFLATED) as archive:
        for target, content, old in changed:
            key = "agents/" + target.name if old is not None else None
            if key:
                archive.writestr(key, old)
            records.append({"target": str(target), "backup_key": key, "installed_sha256": digest(content)})
        archive.writestr("RESTORE_MAP.json", json.dumps(records, ensure_ascii=False, indent=2))
    written = []
    try:
        for target, content, old in changed:
            safe_target(target)
            target.parent.mkdir(parents=True, exist_ok=True)
            current = target.read_bytes() if target.is_file() else None
            if current != old:
                raise RuntimeError(f"Changed while installing; refusing overwrite: {target}")
            atomic_write(target, content)
            written.append((target, old))
        for target, content, _, _ in entries:
            if target.read_bytes() != content:
                raise RuntimeError(f"Readback mismatch: {target}")
    except Exception:
        for target, old in reversed(written):
            if old is None:
                target.unlink(missing_ok=True)
            else:
                atomic_write(target, old)
        raise
    return {"installed": True, "changed": len(changed), "verified": 13, "backup": str(backup), "skills_written": 0, "config_changes": 0}


def restore(backup):
    with zipfile.ZipFile(backup) as archive:
        records = json.loads(archive.read("RESTORE_MAP.json"))
        for record in records:
            target = Path(record["target"])
            safe_target(target)
            if not target.is_file() or digest(target.read_bytes()) != record["installed_sha256"]:
                raise RuntimeError(f"Changed after install; refusing restore: {target}")
        for record in records:
            target = Path(record["target"])
            if record["backup_key"]:
                atomic_write(target, archive.read(record["backup_key"]))
            else:
                target.unlink()
    return {"restored": True, "files": len(records)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agents-root", type=Path, default=Path.home() / ".codex/agents")
    parser.add_argument("--backup-dir", type=Path, default=Path.home() / ".codex/backups/qa-brandformance")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--replace-existing", action="store_true")
    parser.add_argument("--restore", type=Path)
    args = parser.parse_args()
    try:
        if args.restore:
            result = restore(args.restore.expanduser())
        else:
            # Keep lexical path for symlink checks rather than resolving it first.
            result = install(args.agents_root.expanduser().absolute(), args.backup_dir.expanduser().absolute(), dry_run=args.dry_run, replace_existing=args.replace_existing, check=args.check)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.check and not result["valid"]:
            raise SystemExit(1)
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"error": str(exc), "installed": False}, ensure_ascii=False))
        raise SystemExit(1)
