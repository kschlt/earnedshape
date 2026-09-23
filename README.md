# earnedshape

**A protocol for human–AI discovery work — understanding that has earned its robustness.**

> **Pre-implementation.** The specification exists. Nothing here is installable yet, and almost none of it has been tested in a real, instrumented run. That distinction is kept visible on purpose.

## The problem

Discovery is the work between *something is wrong here* and *we know what to build*. It is where the expensive mistakes happen, because a wrong frame survives into everything downstream.

Done alone, it is slow, and you cannot see around your own assumptions.

Done with an AI, it is fast — and it fails in a particular way. The AI answers completely, fluently, immediately. A plausible abstraction gets repeated; the repetition starts to feel like agreement; at some point it has become a commitment nobody made. The reasoning scrolls away with the transcript. What survives is a polished document whose decisions the person who has to defend them cannot actually defend.

Better prompts do not fix this. The failure is not that the AI knows too little. It is that **fluency is indistinguishable from agreement**, and nothing in an ordinary chat keeps them apart.

## What earnedshape adds

A protocol that forces the two apart:

- **Objects** — probes, candidates, recommendations, decisions, commitments, concepts, assumptions, deferred questions. A discovery is made of things with a status, not of messages.
- **Status changes only through a recorded transition.** Never through repetition, never through a polished restatement.
- **The commitment act** — a commitment exists only with its rejected alternative, its rationale, and the condition under which it should be reopened. Anything else is a draft, however confident it sounds.
- **Decision rights** — what the AI may do alone, what it may draft, what it may only advise on, and what stays with the human.
- **Meaning before commitment** — a term the AI coins starts as a candidate. Fluent vocabulary is not shared understanding until it has been tested against cases.
- **Challenge before convergence** — a model is not ready to commit to until it has survived a deliberate attempt to break it. (Accepted after review; the protocol text follows in v0.2.1.)

The governing rule is inverted from most AI tooling: it optimises for the **next valuable human contribution**, not for the completeness of the AI's answer.

It is not a prompt library, an agent framework, a requirements tool, or a methodology.

## Who it is for

One person doing serious discovery work with an AI, who wants the improvement to accumulate across projects instead of being re-invented in every chat.

It assumes one human, one AI, and a discovery that ends in a handoff. Teams, multiple stakeholders, and discovery inside an existing system are out of scope — declared, rather than discovered later.

## What exists

| | |
|---|---|
| `protocol/` | the specification, technology-independent, including what a run must emit to be checkable at all |
| `capabilities/` | what an adapter would have to do, and how each capability is evaluated |
| `research/` | the synthesis, including a standing section for evidence **against** the premise |
| `tools/` | the lint that keeps the protocol layer vendor-free, and the guard that keeps private addresses out of the public history |
| `examples/` | one real commitment and one overruled challenge, recorded in the protocol's shape |
| `docs/review/` | the adversarial review of v0.2 and what happened to each of its change proposals |

No adapter. No instrumented run. The conformance matrix — which capability is realisable where — is empty because filling it with guesses would be worse than leaving it blank.

Start with [`docs/overview.md`](docs/overview.md).

## Using it today

There is nothing to install. What you can do now:

- **Use the protocol as a checklist** against your own AI-assisted discovery: does every commitment have a rejected alternative and a revisit condition, did the AI's vocabulary become yours without anyone deciding it?
- **Read [`examples/naming-decision.md`](examples/naming-decision.md)** to see the two central records on a real decision.
- **Attack it.** Open an issue with a contradiction, an unfalsifiable rule, or a discovery where this would have cost more than it returned.

## How it was developed

Two discoveries done with an AI, each analysed afterwards as an evidence case; four focused research reports; a protocol revised once on their basis; an [adversarial review](docs/review/2026-09-adversarial-review-v0.2.md) of that revision with 25 findings and 15 change proposals, each proposal [dispositioned](docs/review/disposition.md); then an observation model and a capability catalogue so that the protocol's claims can be measured at all. [`docs/provenance.md`](docs/provenance.md) has the timeline and says what is still private and why.

## What's next

Phase 1 finds out what can actually be observed before anything steers: first, whether a conversational turn can be recorded automatically in Claude Code, then state across sessions, skipped capabilities and the cost of enforcement. The instrument for the first question is built; the run is pending. See [`docs/phase-1-feasibility.md`](docs/phase-1-feasibility.md).

## What the evidence actually says

Two retrospective cases, the second derived from the first, so recurrence between them is dependent rather than replicated. No independent case yet.

The study closest to this protocol's target task — LLM support for problem framing, N=280 ([Shin et al., CHI 2025](https://doi.org/10.1145/3706598.3713273)) — found no improvement in frame quality, a widened gap between experienced and inexperienced practitioners, and lower perceived agency among novices. So the honest claim is not that research supports this:

> earnedshape is a bet that the **design of the interaction** — not the presence of the AI — decides the outcome. The bet is plausible, unproven, and the project is built so that it can lose.

Every source the research synthesis relies on is listed and checked in [`research/REFERENCES.md`](research/REFERENCES.md), including where the support is thinner than the wording. Open findings against this baseline, including two reported by the project's own lint against its own protocol, are in [`docs/known-findings.md`](docs/known-findings.md).

## Contributing

The scarcest contribution is evidence, not features — especially a discovery where the protocol cost more than it returned. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

Prose is CC BY 4.0, code is MIT ([`docs/licensing.md`](docs/licensing.md)). Protocol `v0.2`; protocol and adapter maturity are versioned separately. "Human–AI Discovery Protocol", still the heading of [`protocol/01_PROTOCOL_V0.2.md`](protocol/01_PROTOCOL_V0.2.md), is the earlier working title; the protocol is now called earnedshape.
