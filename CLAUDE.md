<!-- aos:begin id=task-workflow rev=1 managed by aos touchpoint writer - do not edit by hand -->
This project's backlog, session protocol, and workflow tooling are managed by **aos** (the meta-workflow layer mounted at `.aos/`). Machinery lives at `.aos/sys/`; the authoritative session protocol is `.aos/sys/core/CLAUDE.md`. Instance state (backlog, specs, work-log) lives in the nested state repo at `.aos/` (host-ignored, its own git history). Do not edit this managed region by hand.
<!-- aos:end id=task-workflow -->

# earnedshape

This repository is public-facing. Everything committed here, including commit messages, is written for outside readers.

- Treat the repository as public, including its full history: a pushed commit stays retrievable even after a rewrite. Commits use a noreply address only: the GitHub noreply address for people, `noreply@anthropic.com` for agent commits. Before every commit, run `python3 tools/public_guard.py . --commits HEAD --deny-file .aos/public-deny.txt`; it is the configured quality command. The deny file is private and stays in the state repository: never copy its terms into this repository, a commit message, a pull request or a comment.
- Keep `protocol/` vendor-free. `python3 tools/boundary_lint.py .` enforces the layer cut and is the CI gate; run it before every commit.
- Nothing private enters this repository: no personal or critical content, no employer or client names, no content from discovery runs. The author's own projects may be named with a one-line description (see `docs/provenance.md`).
- Spike code stays in the private working repository. This repository records spike questions, status and results (`docs/phase-1-feasibility.md`, `capabilities/CONFORMANCE.md`).
- Research claims cite an entry in `research/REFERENCES.md`. A field that could not be checked stays marked "not confirmed", with the reason.
