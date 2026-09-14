# Contributing

The scarcest contribution here is **evidence**, not features.

## What helps most

**A discovery you actually ran.** What the protocol got right, and specifically where it cost more than it returned. Negative results are what this project is short of — it currently has two retrospective cases, the second derived from the first, and no independent one.

**An attack on the baseline.** Contradictions, unsupported certainty, hidden assumptions, places where a rule is unfalsifiable as written. The protocol has had one adversarial review. That is not close to enough, and the review that found the most was the one that treated the documents as adversarially as they treat their own subject.

**A capability that cannot be observed.** If a rule in `protocol/` has no path to an event in `protocol/observation-model/`, it cannot be evaluated and should be marked as such rather than left looking like a mechanism awaiting evidence.

## What to expect

Proposals are treated the way the protocol treats any tentative structure: a proposal stays distinguishable from an accepted commitment, and a change to a rule states the observation that motivated it, the expected mechanism, the known downside, and what remains hypothesis.

Disagreement is recorded rather than resolved by attrition. An overruled objection stays visible.

## Practical

- Run `python3 tools/boundary_lint.py .` before proposing a change. It fails on new findings only; the accepted ones are in `tools/known-findings.txt` with reasons in `docs/known-findings.md`.
- Prose is CC BY 4.0, code is MIT — see `docs/licensing.md`.
- Please do not include private project material in an evidence contribution. What is useful is the shape of what happened, never the content of what you were working on.
