# Overview — how the pieces relate

Four layers. The separation is the design, not the filing system: each answers a different question, and collapsing any two of them is the failure this project exists to avoid.

```
protocol/          what discovery should do          technology-independent, normative
capabilities/      what an adapter must do           derived from the protocol, vendor-free
adapters/          how one environment does it       does not exist yet
runs               what actually happened            private, never in this repository
```

## protocol/

The normative specification. What objects exist in a discovery, what status each carries, who may change that status, what the AI may do without asking. It names no product, no harness and no vendor — enforced by `tools/boundary_lint.py`, whose findings are visible in `docs/known-findings.md`.

`protocol/observation-model/` is part of the protocol because *what a run must emit* is a normative question. How it is captured is not.

## capabilities/

The bridge. A capability is derived from a protocol rule, states a required observable behaviour, and can be enforced, measured and rolled back. Each entry names what it must emit, how it is evaluated on both levels, and what an honest negative result would look like.

Two things this layer makes possible that prose cannot:

**An enforcement ladder.** L0 protocol text · L1 guidance injected into a session · L2 an invocable skill · L3 something deterministic that cannot be skipped. Never start above L1. And take the compliance measurement *before* hardening — at L3 compliance is trivially total, and the question "would it have happened anyway?" can never be asked again.

**Two evaluation levels.** Level 1 asks whether the mechanism fired when it should. Level 2 asks whether it produced the promised benefit. A level-2 null result is uninterpretable when level-1 fidelity is low, which is the most common way a working method gets declared a failure.

## capabilities/CONFORMANCE.md

Per environment: is a capability realised, at what enforcement level, and is its firing observable. Three separate questions, deliberately not collapsed. **An empty observability cell is a hard gate — no evaluation claim may be made about that capability in that environment.**

It is currently empty on purpose. Filling it with guesses would be worse than leaving it blank.

## research/

Curated synthesis, including a standing section for evidence *against* the premise. That section is not empty and is not meant to be.

## Maturity

Protocol maturity and adapter maturity are tracked separately and move at different speeds. Today: protocol `v0.2`, no adapter, no instrumented run, conformance matrix empty. The honest summary is that the specification layer exists and nothing has been tested.
