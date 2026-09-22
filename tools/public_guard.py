#!/usr/bin/env python3
"""Public-history guard: keeps private addresses and names out of the repository.

This repository is public, and so is every commit in it: file contents,
author and committer identities, and commit messages. A private address
that lands in a pushed commit stays retrievable even after a rewrite, so
the check has to run before the push, and CI repeats it for every commit
that reaches GitHub. Pull request titles, bodies and comments are outside
its reach and need the same care by hand.

Four rules:
  P1  no email address in a tracked file, unless allowlisted
  P2  no commit author or committer email outside the allowlist
  P3  no email address in a commit message, unless allowlisted
  P4  no term from a deny file in a tracked file, a commit message or an
      author or committer name (only with --deny-file)

Allowlisted: GitHub noreply addresses (*@users.noreply.github.com,
noreply@github.com), noreply@anthropic.com (co-author trailers), and
addresses on reserved example domains (example.com/.org/.net, *.example,
*.invalid).

The deny file is private by design: it names what must not appear here,
so it lives outside the repository and is passed in locally. One term per
line, matched case-insensitively as a whole word; a line starting with
`re:` is a regular expression; `#` starts a comment.

Findings are printed with the matched text masked, because CI logs of a
public repository are public too. `--self-test` runs every rule against
built-in samples and a throwaway git repository with known leaks (tracked
file, committer, name, new commit), so CI shows the guard still catches
what it should.

Usage:  python3 tools/public_guard.py [repo_root] [--commits REV]
                                     [--message-file PATH] [--deny-file PATH]
        --commits REV        also check commits reachable from REV (passed
                             to `git log`, e.g. HEAD, --all, origin/main..HEAD)
        --message-file PATH  check a commit message about to be written and
                             the current author and committer identity
                             (for a commit message hook)
        python3 tools/public_guard.py --self-test
Exit:   0 clean, 1 violations found, 2 usage or git error.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
ALLOWED_ADDRESSES = {"noreply@github.com", "noreply@anthropic.com",
                     "git@github.com"}   # the SSH clone host, not a mailbox
ALLOWED_SUFFIXES = (
    "@users.noreply.github.com",
    "@example.com", "@example.org", "@example.net",
    ".example", ".invalid",
)


# `icon@2x.png` is a retina asset name, not an address.
ASSET_RE = re.compile(r"@\d+(?:\.\d+)?x\.(?:png|jpe?g|gif|svg|webp)$", re.I)


def allowed(email: str) -> bool:
    e = email.lower()
    return (e in ALLOWED_ADDRESSES or e.endswith(ALLOWED_SUFFIXES)
            or bool(ASSET_RE.search(e)))


def mask(text: str) -> str:
    """Keep enough to locate the finding without republishing it."""
    return text[0] + "*" * (len(text) - 2) + text[-1] if len(text) > 2 else "*" * len(text)


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], check=True,
                          capture_output=True).stdout.decode("utf-8", "replace")


def load_deny(path: Path):
    patterns = []
    for ln in path.read_text().splitlines():
        term = ln.split("#", 1)[0].strip()
        if not term:
            continue
        if term.startswith("re:"):
            patterns.append(re.compile(term[3:].strip(), re.I))
        else:
            left = r"\b" if re.match(r"\w", term) else ""
            right = r"\b" if re.search(r"\w$", term) else ""
            patterns.append(re.compile(left + re.escape(term) + right, re.I))
    return patterns


def scan_text(text: str, where, deny, email_rule: str):
    """Yield (location, message) for emails and deny terms in a block of text."""
    for n, line in enumerate(text.splitlines(), 1):
        for m in EMAIL_RE.finditer(line):
            if not allowed(m.group(0)):
                yield where(n), f"{email_rule} email address {mask(m.group(0))!r}"
        for p in deny:
            for m in p.finditer(line):
                yield where(n), f"P4 deny-listed term {mask(m.group(0))!r}"


def rule_tracked_files(root: Path, deny):
    out = []
    for rel in git(root, "ls-files", "-z").split("\0"):
        path = root / rel
        if not rel or not path.is_file():
            continue
        data = path.read_bytes()
        if b"\0" in data:            # binary
            continue
        out += scan_text(data.decode("utf-8", "replace"),
                         lambda n, rel=rel: f"{rel}:{n}", deny, "P1")
    return out


def check_identity(where: str, role: str, name: str, email: str, deny):
    out = []
    if not allowed(email):
        out.append((where, f"P2 {role} email {mask(email)!r} is not a noreply address"))
    for p in deny:
        for m in p.finditer(name):
            out.append((where, f"P4 deny-listed term {mask(m.group(0))!r} in {role} name"))
    return out


def rule_commits(root: Path, rev: str, deny):
    out = []
    log = git(root, "log", "--format=%H%x00%an%x00%ae%x00%cn%x00%ce%x00%B%x1e", rev)
    for rec in log.split("\x1e"):
        rec = rec.strip("\n")
        if not rec:
            continue
        sha, an, ae, cn, ce, body = rec.split("\0", 5)
        where = f"commit {sha[:7]}"
        out += check_identity(where, "author", an, ae, deny)
        out += check_identity(where, "committer", cn, ce, deny)
        out += scan_text(body, lambda n, where=where: f"{where} message:{n}", deny, "P3")
    return out


def rule_message_file(root: Path, path: Path, deny):
    out = list(scan_text(path.read_text(), lambda n: f"commit message:{n}", deny, "P3"))
    for role, var in (("author", "GIT_AUTHOR_IDENT"), ("committer", "GIT_COMMITTER_IDENT")):
        m = re.match(r"(.*) <([^>]*)>", git(root, "var", var).strip())
        if m:
            out += check_identity("new commit", role, m.group(1), m.group(2), deny)
    return out


def self_test():
    """Each rule must still fire on a known-bad sample and stay quiet on a good one.

    The bad samples are assembled at run time, so this file itself stays clean.
    """
    at = "@"
    deny = [re.compile(r"\bcanary-term\b", re.I)]
    where = lambda n: f"sample:{n}"
    cases = [
        ("P1 fires", list(scan_text(f"mail jane.doe{at}mail.test.de", where, [], "P1")), 1),
        ("P1 allowlist", list(scan_text(f"a{at}example.com 1+u{at}users.noreply.github.com "
                                        f"git{at}github.com:o/r.git icon{at}2x.png",
                                        where, [], "P1")), 0),
        ("P2 fires", check_identity("c", "author", "x", f"me{at}private.test.de", []), 1),
        ("P2 noreply", check_identity("c", "author", "x", f"noreply{at}github.com", []), 0),
        ("P3 fires", list(scan_text(f"reach me: x{at}corp.io", where, [], "P3")), 1),
        ("P4 fires", list(scan_text("a Canary-Term here", where, deny, "P3")), 1),
        ("P4 whole word", list(scan_text("canary-terms", where, deny, "P3")), 0),
        ("asset-shaped address", list(scan_text(f"j.doe{at}corp-mail.de.pdf", where, [], "P1")), 1),
    ]
    cases += git_cases(at, deny)
    failed = [name for name, got, want in cases if len(got) != want]
    if mask(f"secret{at}x.io") != "s*********o":
        failed.append("mask hides the middle")
    for name in failed:
        print(f"SELF-TEST FAILED  {name}")
    print(f"self-test: {len(failed)} of {len(cases) + 1} checks failed.")
    return 1 if failed else 0


def git_cases(at, deny):
    """Run the git-reading rules against a throwaway repository with known leaks.

    The sample repository gets its own environment: no variable that points
    git at another repository, no global or system config (signing, hooks,
    templates), and identities set per commit.
    """
    bad, good = f"me{at}private.test.de", f"1+u{at}users.noreply.github.com"
    saved = dict(os.environ)
    for k in list(os.environ):
        if k.startswith("GIT_"):
            del os.environ[k]
    os.environ.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")

    def ident(author_email, committer_email, committer_name="u"):
        os.environ.update(GIT_AUTHOR_NAME="u", GIT_AUTHOR_EMAIL=author_email,
                          GIT_COMMITTER_NAME=committer_name,
                          GIT_COMMITTER_EMAIL=committer_email)

    def commit(text):
        git(root, "commit", "-q", "--no-verify", "--allow-empty", "-m", text)

    try:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            git(root, "init", "-q")
            (root / "leak.md").write_text(f"contact {bad}\n")
            git(root, "add", "leak.md")
            ident(good, good)
            commit("clean")
            ident(bad, good)
            commit(f"author leak, reach me: x{at}corp.io")   # P2 author + P3
            ident(good, bad)
            commit("committer leak")                         # P2 committer
            ident(good, good, committer_name="Canary-Term")
            commit("name leak")                              # P4 name
            message = root / "message.txt"
            message.write_text(f"reach me: x{at}corp.io\n")
            ident(bad, good)
            return [
                ("git: tracked file", rule_tracked_files(root, []), 1),
                ("git: author, message, committer and name", rule_commits(root, "HEAD", deny), 4),
                ("git: new commit message and identity", rule_message_file(root, message, []), 2),
            ]
    except (OSError, subprocess.CalledProcessError) as e:
        return [(f"git: could not build the sample repository ({type(e).__name__})", [], 1)]
    finally:
        os.environ.clear()
        os.environ.update(saved)


def parse_args(argv):
    opts, rest = {}, []
    it = iter(argv)
    for a in it:
        if a in ("--commits", "--message-file", "--deny-file"):
            val = next(it, None)
            if val is None:
                raise SystemExit(f"{a} needs a value")
            opts[a] = val
        elif a.startswith("--") and a not in ("--",):
            raise SystemExit(f"unknown option {a}")
        else:
            rest.append(a)
    if len(rest) > 1:
        raise SystemExit("at most one repo_root")
    return Path(rest[0] if rest else ".").resolve(), opts


def main():
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    try:
        root, opts = parse_args(sys.argv[1:])
        deny = []
        if "--deny-file" in opts:
            deny_path = Path(opts["--deny-file"])
            if not deny_path.is_file():
                raise SystemExit(f"deny file not found: {deny_path}")
            deny = load_deny(deny_path)
    except (SystemExit, re.error) as e:
        print(f"usage error: {e}", file=sys.stderr)
        return 2
    try:
        findings = rule_tracked_files(root, deny)
        if "--commits" in opts:
            findings += rule_commits(root, opts["--commits"], deny)
        if "--message-file" in opts:
            findings += rule_message_file(root, Path(opts["--message-file"]), deny)
    except subprocess.CalledProcessError as e:
        err = e.stderr.decode("utf-8", "replace").strip().splitlines()
        print(f"git error: git {' '.join(e.cmd[3:4])} failed"
              f"{': ' + err[0] if err else ''}", file=sys.stderr)
        return 2
    except OSError as e:
        print(f"usage error: {e.strerror}: {Path(e.filename).name if e.filename else ''}",
              file=sys.stderr)
        return 2
    for where, what in findings:
        print(f"FOUND    {where}: {what}")
    scope = "tracked files" + (f", commits {opts['--commits']}" if "--commits" in opts else "")
    print(f"\n{len(findings)} finding(s) in {scope}"
          f"{'' if deny else ' (no deny file: P4 not checked)'}.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
