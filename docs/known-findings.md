# Known findings

Open findings against the current baseline, kept in the open rather than fixed quietly. The boundary lint reports them as `known` and fails only on new ones; `tools/known-findings.txt` is the list it reads.

A project whose method is "make the unresolved visible" should not ship a clean-looking repository with a private defect list.

## KF-1 · `protocol/06` names a specific tool in a rule

> "replace internal ChatGPT citations"

The rule is about citation provenance, not about one product. A technology-independent layer should say "internal research-tool citations".

**Status:** open. The protocol is not edited without an accepted change proposal, and this one has not been through that process.

## KF-2 · `protocol/07` section B does not belong in the protocol

`T-03` names a specific harness as a candidate for the first binding. Taken alone this is a naming issue; the real finding is a layering one. Section B of `07` is a register of **deferred technical decisions** — repository topology, state serialisation, skill architecture, release workflow. Those are project decisions, not protocol semantics, and their presence is the only reason the normative layer names a harness at all.

**Proposed fix:** move section B out of `protocol/` into project documentation, leaving `07` with protocol decisions and open protocol questions.
**Status:** open, and the more consequential of the two.

## What this file is not

It is not a bug tracker and not a backlog. It holds findings against the *published baseline* that a reader would otherwise have to discover for themselves — the ones an honest reviewer would raise on first reading. Findings that get fixed leave this file and appear in the changelog instead.
