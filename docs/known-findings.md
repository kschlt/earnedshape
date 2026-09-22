# Known findings

Open findings against the current baseline, kept in the open rather than fixed quietly. The boundary lint reports them as `known` and fails only on new ones; `tools/known-findings.txt` is the list it reads.

A project whose method is "make the unresolved visible" should not ship a clean-looking repository with a private defect list.

## KF-1 · `protocol/06` names a specific tool in a rule

> "replace internal ChatGPT citations"

The rule is about citation provenance, not about one product. A technology-independent layer should say "internal research-tool citations".

**Status:** open. The protocol is not edited without an accepted change proposal, and this one has not been through that process.

## KF-3 · `research/` states some claims more strongly than their sources support

The citation check of September 2026 ([`research/REFERENCES.md`](../research/REFERENCES.md)) found every cited work (a few bibliographic fields remain unconfirmed and are marked there), and found that several items under "strongly supported" in `research/01` §2, and a few statements in `research/02`, rest on practitioner literature, a single study, or the project's own inference. The clearest cases: *language and model can co-evolve* (method literature only), *AI is valuable for articulation, search, synthesis and critique* (articulation and drafting are supported, synthesis rests on one preprint, search and critique are not covered), and *human situated input is epistemically special* (a normative reading of requirements research).

**Proposed fix:** a pass over `research/01` §2 (not part of the v0.2.1 consolidation) that moves these items out of "strongly supported" or narrows their wording, with the change recorded here and in the changelog.
**Status:** open. The claims are marked in place and listed in full in `REFERENCES.md`; the wording itself is unchanged until that pass.

## What this file is not

It is not a bug tracker and not a backlog. It holds findings against the *published baseline* that a reader would otherwise have to discover for themselves — the ones an honest reviewer would raise on first reading. Findings that get fixed leave this file and appear in the changelog instead.
