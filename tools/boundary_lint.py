#!/usr/bin/env python3
"""Draft boundary lint for the layer cut described in 10_PROJECT_SETUP §2.

Doc 10 argues the protocol/adapter boundary should be enforced by a check over
stable capability IDs rather than by a repository boundary. That argument was
made without an implementation, which made it an assertion. This is the
implementation, deliberately small and disposable.

Three rules:
  R1  no file under a protocol root may name a vendor, product or harness
  R2  every CAP-nn referenced outside the catalogue must resolve to an entry
  R3  every capability marked core must appear in the conformance matrix

Usage:  python3 tools/boundary_lint.py [repo_root]
Exit:   0 clean, 1 violations found.
"""
import re
import sys
from pathlib import Path

VENDORS = [
    "claude", "anthropic", "chatgpt", "openai", "gpt-4", "gpt-5", "gemini",
    "copilot", "cursor", "langchain",
]
# Roots that must stay technology-independent, in this repo and in the target layout.
PROTOCOL_ROOTS = ["protocol"]
CATALOGUE = "capabilities/catalogue.md"
MATRIX = "capabilities/CONFORMANCE.md"
CAP_RE = re.compile(r"\bCAP-\d{2}\b")


def rule_no_vendors(root: Path):
    """A technology-independent layer may not state a rule in vendor terms.

    Two exemptions, learned from the first run of this check:
      - fenced blocks, where a vendor name is a VALUE a field may hold
        (a schema that records which surface a run used is data, not a
        vendor-conditional rule);
      - a line carrying the marker `lint:vendor-ok`, for a deliberate
        non-normative aside.
    """
    out = []
    pattern = re.compile("|".join(re.escape(v) for v in VENDORS), re.I)
    for base in PROTOCOL_ROOTS:
        for path in sorted((root / base).rglob("*.md")) if (root / base).exists() else []:
            fenced = False
            for n, line in enumerate(path.read_text().splitlines(), 1):
                if line.lstrip().startswith("```"):
                    fenced = not fenced
                    continue
                if fenced or "lint:vendor-ok" in line:
                    continue
                for m in pattern.finditer(line):
                    out.append((f"{path.relative_to(root)}:{n}",
                                f"R1 vendor name {m.group(0)!r} in a technology-independent layer"))
    return out


def rule_ids_resolve(root: Path):
    cat = root / CATALOGUE
    if not cat.exists():
        return [(CATALOGUE, "R2 catalogue not found")]
    defined = set(CAP_RE.findall(cat.read_text()))
    out = []
    for path in sorted(root.rglob("*.md")):
        rel = str(path.relative_to(root))
        if rel in (CATALOGUE,) or rel.startswith(("docs/known-findings",)):
            continue
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if "lint:id-ok" in line:      # a deliberate reference to a retired or never-allocated id
                continue
            for cap in CAP_RE.findall(line):
                if cap not in defined:
                    out.append((f"{rel}:{n}", f"R2 {cap} does not resolve to a catalogue entry"))
    return out


def rule_core_in_matrix(root: Path):
    cat, mat = root / CATALOGUE, root / MATRIX
    if not (cat.exists() and mat.exists()):
        return [(MATRIX, "R3 catalogue or matrix not found")]
    core = set()
    for block in cat.read_text().split("\n### ")[1:]:
        cap = CAP_RE.search(block)
        if cap and re.search(r"\*\*class\*\*[^\n]*", block) and "core" in block.split("\n")[1].lower() + block.lower()[:400]:
            if re.search(r"\bcore\b", block[:400], re.I):
                core.add(cap.group(0))
    in_matrix = set(CAP_RE.findall(mat.read_text()))
    return [(MATRIX, f"R3 core capability {c} missing from the conformance matrix")
            for c in sorted(core - in_matrix)]


def load_known(root: Path):
    """Known findings are listed, not hidden.

    A baseline keeps CI meaningful: it fails on anything NEW while the
    accepted findings stay visible in a file anyone can read, with their
    reasons in docs/known-findings.md. An entry is `path:line: rule`.
    """
    f = root / "tools/known-findings.txt"
    if not f.exists():
        return set()
    return {ln.split("#")[0].strip() for ln in f.read_text().splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")}


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings = rule_no_vendors(root) + rule_ids_resolve(root) + rule_core_in_matrix(root)
    known = load_known(root)
    new = []
    for where, what in findings:
        key = f"{where}: {what.split(' ', 1)[0]}"
        if key in known:
            print(f"known    {where}: {what}")
        else:
            print(f"NEW      {where}: {what}")
            new.append(key)
    print(f"\n{len(findings)} finding(s), {len(new)} new.")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
