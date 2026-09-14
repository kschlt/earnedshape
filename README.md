# earnedshape

**A protocol for human–AI discovery work — understanding that has earned its robustness.**

> **Status: pre-implementation.** The protocol is specified; almost none of it has been tested in a real, instrumented run. Nothing here is installable yet. This README says exactly what is known, what is guessed, and what is unproven, because that distinction is the point of the project.

## The problem

Working through an ambiguous problem with an AI is fast and often worse than it looks.

The AI answers completely, fluently, immediately. A plausible abstraction gets repeated, the repetition starts to feel like agreement, and at some point it has become a commitment nobody ever made. The transcript scrolls away; the next session starts without the reasoning. What survives is a polished document whose decisions cannot be defended by the person who has to defend them.

The usual response — better prompts, longer answers, more autonomy — makes this worse, because the failure is not that the AI knows too little. It is that fluency is indistinguishable from agreement, and nothing in an ordinary chat keeps them apart.

## What earnedshape is

A technology-independent protocol that defines what exists in a discovery and what it takes to change its status:

- **objects** — probes, candidates, recommendations, decisions, commitments, concepts, assumptions, deferred questions;
- **status** — and the rule that status changes only through a recorded transition, never through repetition;
- **decision rights** — what the AI may do alone, what it may draft, what it may only advise on, and what the human owns;
- **the commitment act** — a commitment exists only with its rejected alternative, its rationale and the condition under which it should be revisited.

It optimises for the next valuable human contribution, not for the completeness of the AI's answer. It treats a polished AI response during exploration as a risk to be managed rather than a result to be celebrated.

It is **not** a prompt library, an agent framework, a multi-agent platform, a requirements tool, or a methodology.

## Who it is for

One person doing serious discovery work with an AI, who wants the AI to stop flattening their thinking — and wants that improvement to accumulate across projects instead of being re-invented in every chat.

It assumes one human, one AI, and a discovery that ends in a handoff. Teams, multiple stakeholders and discovery inside an existing system are out of scope today, and that boundary is declared rather than discovered later.

## What is implemented

**Nothing runnable.** No adapter, no plugin, no skill.

What exists is the specification layer: the protocol, an observation model defining what a run must emit, and a capability catalogue naming what an adapter would have to do and how each capability would be evaluated. The conformance matrix — which capability is realisable in which environment — is deliberately empty until feasibility spikes fill it with demonstrations rather than guesses.

## What is experimental

Most of it. The protocol is a versioned hypothesis, and the mechanisms below are named as untested rather than presented as practice:

adaptive routing · the human-first trigger · the probe debrief · the shared-language lifecycle · terminology provenance · the scenario gate before canonicalisation · persistent state beating implicit memory · the evaluation metrics as predictors of anything.

The hypothesis register lists each claim with what it actually rests on.

## What evidence exists

Two retrospective cases: a product discovery, and the meta-discovery that produced this protocol. The second was derived from the first, so recurrence between them is **dependent, not replication**. An independent third case is the next evidence milestone and has not been run.

The research layer carries a standing section for evidence **against** the premise, and it is not empty. The study closest to this protocol's target task — LLM support for problem framing, N=280 — found no improvement in frame quality, a widened gap between experienced and inexperienced practitioners, and lower perceived agency among novices. The broad meta-analysis of human–AI combination finds average synergy relative to the better single actor to be negative.

So the honest claim is not that research supports this protocol. It is:

> The closest study found no benefit, and the broad evidence on human–AI collaboration is unflattering. earnedshape is a bet that the *design of the interaction* — not the presence of the AI — decides the outcome. The bet is plausible and unproven, and the project is built so that it can lose.

## What you can try today

Read it, and argue with it. Three parts stand alone:

- **the protocol** — usable as a checklist against your own AI-assisted discovery, with no tooling;
- **the capability catalogue** — a worked example of turning a method into things that can be enforced and measured;
- **the analogy records** — the project applying its own boundary check to the four frameworks it imports, including the two places where that check found real problems.

## How to contribute

The most valuable contribution is **evidence**, not features: a discovery you ran, what the protocol got right, and specifically where it cost more than it returned. Negative results are the ones this project is short of.

Contradictions, unsupported certainty and hidden assumptions are equally welcome. The protocol has survived one adversarial review; it is not close to enough.

## Layout

```
protocol/              the normative specification, technology-independent
  observation-model/   what a run must emit for any of this to be checkable
capabilities/          what an adapter must do, and how each is evaluated
research/              curated synthesis, including evidence against the premise
tools/                 the boundary lint that keeps the protocol layer vendor-free
docs/                  overview, licensing, known findings
```

Open findings against this baseline are listed in [`docs/known-findings.md`](docs/known-findings.md) rather than kept privately. Two of them are reported by the project's own lint against its own protocol.

## Licensing

Prose is **CC BY 4.0**, code is **MIT**. The split and the reason for it are in [`docs/licensing.md`](docs/licensing.md) — briefly: adaptations are welcome, and attribution is what keeps a result traceable to the version of the rule that produced it.

## Versioning and maturity

Protocol maturity and adapter maturity are tracked separately and move at different speeds. The protocol is `v0.2`. No adapter exists. A protocol release states the changed rule, the observation that motivated it, the expected mechanism, the known downside, and what remains hypothesis.
