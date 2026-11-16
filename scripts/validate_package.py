#!/usr/bin/env python3
"""Validate marketplace, portable plugin, source preservation and packaged paths."""
import hashlib
import json
from pathlib import Path
import re
import tomllib
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent


def validate(root=ROOT):
    errors = []
    market = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    entry = market["plugins"][0]
    relative = entry["source"]["path"]
    plugin = (root / relative).resolve()
    if not relative.startswith("./") or not plugin.is_relative_to(root.resolve()):
        errors.append("marketplace source escapes repository")
    manifest = json.loads((plugin / "plugin.json").read_text())
    if manifest["name"] != entry["name"] or manifest["version"] != (root / "VERSION").read_text().strip():
        errors.append("plugin identity/version mismatch")
    setup = manifest["extensions"]["com.openai"]["onboardingSkill"]
    if not (plugin / setup).is_file():
        errors.append("missing onboarding skill")
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    names = []
    for skill in skills:
        text = skill.read_text()
        header = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not header:
            errors.append(f"missing skill metadata: {skill.parent.name}")
            continue
        name = re.search(r"^name:\s*(.+)$", header[1], re.M)
        desc = re.search(r"^description:\s*(.+)$", header[1], re.M)
        if not name or not desc or name[1].strip() != skill.parent.name:
            errors.append(f"invalid skill metadata: {skill.parent.name}")
        else:
            names.append(name[1].strip())
    if len(names) != 15 or len(set(names)) != 15:
        errors.append("expected 14 core skills plus one setup skill")
    links = 0
    for file in root.rglob("*.md"):
        if ".git" in file.parts:
            continue
        for dest in re.findall(r"\]\(([^)]+)\)", file.read_text()):
            dest = unquote(dest.strip().strip("<>").split("#", 1)[0])
            if not dest or "://" in dest or dest.startswith("mailto:"):
                continue
            links += 1
            if not (file.parent / dest).exists():
                errors.append(f"broken link: {file.relative_to(root)} -> {dest}")
    agents = list((plugin / "assets/agents").glob("*.toml"))
    if len(agents) != 13:
        errors.append("expected 13 custom agents")
    for file in agents:
        data = tomllib.loads(file.read_text())
        if set(data) != {"name", "description", "developer_instructions"} or data["name"] not in names or data["name"] != file.stem:
            errors.append(f"invalid agent: {file.name}")
    sources = json.loads((root / "SOURCE_MANIFEST.json").read_text())["source_files"]
    for item in sources:
        file = plugin / item["path"]
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != item["sha256"]:
            errors.append(f"core changed from approved package: {item['path']}")
    for file in plugin.rglob("*"):
        if file.is_symlink():
            errors.append(f"symlink in package: {file.relative_to(root)}")
        if file.is_file() and "__pycache__" not in file.parts:
            body = file.read_text()
            if "/Users/sakai" in body or "__QA_SKILLS_ROOT__" in body:
                errors.append(f"non-portable owner path: {file.relative_to(root)}")
            if re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{30,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)", body):
                errors.append(f"credential-like content: {file.relative_to(root)}")
    checksum = root / "PACKAGE_MANIFEST.json"
    if not checksum.exists():
        errors.append("missing package checksums")
    else:
        for rel, sha in json.loads(checksum.read_text())["files"].items():
            file = root / rel
            if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != sha:
                errors.append(f"checksum mismatch: {rel}")
    return {"valid": not errors, "version": manifest["version"], "business_skills": 14, "setup_skills": 1, "agents": len(agents), "links_checked": links, "preserved_core_files": len(sources), "errors": errors}


if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["valid"] else 1)
