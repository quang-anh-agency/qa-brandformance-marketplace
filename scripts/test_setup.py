#!/usr/bin/env python3
"""Exercise agent installation/recovery on isolated temporary targets only."""
import importlib.util
from pathlib import Path
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("qa_setup", ROOT / "plugins/qa-brandformance/scripts/setup_agents.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def snapshot(path):
    return {str(f.relative_to(path)): f.read_bytes() for f in path.rglob("*") if f.is_file()}


with tempfile.TemporaryDirectory(prefix="qa-team-setup-") as temp:
    root = Path(temp).resolve()
    agents = root / "agents"
    agents.mkdir()
    sentinel = agents / "unrelated.toml"
    sentinel.write_text("preserve this unrelated file")
    before = snapshot(agents)
    preview = module.install(agents, root / "backups", dry_run=True)
    assert preview["can_install_without_replacement"] and snapshot(agents) == before
    result = module.install(agents, root / "backups")
    assert result["verified"] == 13 and result["changed"] == 13
    assert module.install(agents, root / "backups")["changed"] == 0
    assert module.install(agents, root / "backups", check=True)["valid"]
    assert sentinel.read_text() == "preserve this unrelated file"
    module.restore(result["backup"])
    assert snapshot(agents) == before

    conflict = agents / "qa-reviewer.toml"
    conflict.write_text("owner customized content")
    before = snapshot(agents)
    try:
        module.install(agents, root / "backups")
        raise AssertionError("expected conflict refusal")
    except RuntimeError as exc:
        assert "Existing agents differ" in str(exc)
    assert snapshot(agents) == before
    result = module.install(agents, root / "backups", replace_existing=True)
    module.restore(result["backup"])
    assert snapshot(agents) == before

    result = module.install(agents, root / "backups", replace_existing=True)
    conflict.write_text("new work after installation")
    after_edit = snapshot(agents)
    try:
        module.restore(result["backup"])
        raise AssertionError("expected changed-file refusal")
    except RuntimeError as exc:
        assert "Changed after install" in str(exc)
    assert snapshot(agents) == after_edit

    elsewhere = root / "elsewhere"
    elsewhere.mkdir()
    alias = root / "symlink-agents"
    alias.symlink_to(elsewhere, target_is_directory=True)
    try:
        module.install(alias, root / "backups")
        raise AssertionError("expected symlink refusal")
    except RuntimeError as exc:
        assert "symlink" in str(exc)
    assert not list(elsewhere.iterdir())

    # Fail after several successful writes, while the reviewer's new bytes
    # are being flushed. The customized target and unrelated files must survive.
    failure_root = root / "failure-agents"
    failure_root.mkdir()
    (failure_root / "qa-reviewer.toml").write_text("owner customized reviewer")
    (failure_root / "unrelated.txt").write_text("keep me")
    before_failure = snapshot(failure_root)
    original_atomic = module.atomic_write
    def failing_atomic(target, content):
        if target.name == "qa-reviewer.toml" and content != before_failure[target.name]:
            with patch.object(module.os, "fsync", side_effect=OSError("simulated write failure")):
                return original_atomic(target, content)
        return original_atomic(target, content)
    try:
        with patch.object(module, "atomic_write", side_effect=failing_atomic):
            module.install(failure_root, root / "backups", replace_existing=True)
        raise AssertionError("expected simulated write failure")
    except OSError as exc:
        assert "simulated write failure" in str(exc)
    assert snapshot(failure_root) == before_failure
    assert not list(failure_root.glob(".qa-agent-*"))

print("PASS: dry-run, install/readback, idempotence, exact restore, conflict atomicity, changed-file protection, symlink refusal, mid-write rollback; unrelated files retained")
