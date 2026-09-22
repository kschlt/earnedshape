# Evidence & Research Synthesis — v0.2

> **Amendment note.** Section 2A and the correction inside §2 were added under change proposal **CP-07** of the [adversarial review](../docs/review/2026-09-adversarial-review-v0.2.md), after it found that this curated layer had dropped the disconfirming evidence present in the raw research reports (`source-research/`, unpublished; see [`docs/provenance.md`](../docs/provenance.md)), and had promoted one contested finding to "strongly supported". No other claim in this file was altered. The sources were verified against primaries in September 2026; see §9.

## 1. Evidence architecture

The current baseline is informed by:

> **Note for readers of the public repository.** The evidence cases themselves are **not published here**. They are retrospectives of real projects and need editing for privacy, self-containedness and non-circular evidence logic before they can be released. What follows is the synthesis; the underlying cases are currently unverifiable by an outside reader, and that limitation is part of the claim.

### Process evidence
- Case 01: an object-level product discovery retrospective.
- Case 02: meta-discovery that produced the Human–AI Discovery Protocol.
- Post-hoc Shared Language addendum to Case 02.

### Focused research
- Human Contribution & Interaction Design.
- Problem Framing, Solution Probes & Fixation.
- Evaluation of Human–AI Discovery Protocols.
- Shared Conceptual Language, terminology formation & AI anchoring.

### Prior adjacent design work
- Turn / Adaptive Cognitive Handoff for predominantly autonomous implementation agents — the author's earlier, unpublished design work ([`docs/provenance.md`](../docs/provenance.md)).

None of these alone validates the full protocol.

---

## 2. Strongly supported directions

### Human–AI collaboration is not automatically synergistic
*Sources:* [Vaccaro2024](REFERENCES.md#vaccaro2024), [Bansal2021](REFERENCES.md#bansal2021)

Task allocation and interaction design matter.

### Human situated input remains epistemically special
*Sources:* [Ferrari2016](REFERENCES.md#ferrari2016), [Ferrari2022](REFERENCES.md#ferrari2022) — support is narrower than the heading; see [REFERENCES.md](REFERENCES.md#where-the-support-is-thinner-than-the-wording).

But human experience is evidence, not infallible truth.

### AI can be highly valuable for articulation, search, synthesis and critique
*Sources:* [Mircea2026](REFERENCES.md#mircea2026), [Noy2023](REFERENCES.md#noy2023) — articulation and drafting only; see [REFERENCES.md](REFERENCES.md#where-the-support-is-thinner-than-the-wording).

The correct response to AI anchoring risk is not "AI stays silent".

### Early AI output can influence human exploration/agency
*Sources:* [Qin2025](REFERENCES.md#qin2025), [Wadinambiarachchi2024](REFERENCES.md#wadinambiarachchi2024), [Doshi2024](REFERENCES.md#doshi2024)

Timing and presentation matter.

### Problem and solution can co-evolve
*Sources:* [DorstCross2001](REFERENCES.md#dorstcross2001)

The important protection is against premature commitment.

### Shared terminology reduces coordination cost
*Sources:* [BrennanClark1996](REFERENCES.md#brennanclark1996), [PickeringGarrod2004](REFERENCES.md#pickeringgarrod2004), [GlinzFricker2015](REFERENCES.md#glinzfricker2015) — laboratory tasks, not measured in discovery work.

But lexical agreement does not prove conceptual agreement.

### Language and model can co-evolve
*Sources:* [Evans2003](REFERENCES.md#evans2003) — practitioner literature only.

Important terminology can be part of the conceptual model, not just labels applied afterward.

### Human-computer lexical alignment is real
*Sources:* [Branigan2011](REFERENCES.md#branigan2011), [Ostrand2023](REFERENCES.md#ostrand2023)

This creates a plausible path for AI-originated terminology to become default without explicit conceptual agreement.

### Explanations alone do not guarantee appropriate reliance
*Sources:* [Bansal2021](REFERENCES.md#bansal2021), [Bucinca2021](REFERENCES.md#bucinca2021)

Selective cognitive engagement matters.

### Structured scaffolding can outperform generic chat — *contested*
*Sources:* [Heyman2024](REFERENCES.md#heyman2024), [Luan2025](REFERENCES.md#luan2025); against: [Wadinambiarachchi2024](REFERENCES.md#wadinambiarachchi2024)

One experiment (Supermind Ideator) found a structured GenAI scaffold produced solutions rated more innovative than both generic chat and human-only work. `source-research/01` rates this evidence **medium and explicitly contradictory**, because the fixation studies point the other way on adjacent tasks. It was previously listed here without that qualification, which overstated it. It remains the most direct support for the protocol's central bet, and it comes from ideation, not discovery.

---

## 2A. Evidence against this protocol's premise

A curated layer that only carries supporting evidence is not a synthesis. This section exists so that the strongest counter-evidence is visible at the same altitude as the support, and it is a standing section: **every future research pass must either add to it or state explicitly that it found nothing to add.**

### The closest study to the target task found no benefit
*Sources:* [Shin2025](REFERENCES.md#shin2025)

Shin et al. (CHI 2025, N=280) compared free LLM use, direct frame generation, a theory-guided structured LLM method, and a control condition. It found **no improvement in problem-frame quality** from LLM use; the competence gap between experienced and inexperienced designers **widened**; and inexperienced participants reported **lower perceived agency**. Of all the evidence in this pack, this is the study nearest to what this protocol is for — problem framing, by individuals, with an LLM — and it is negative.

It appears in `source-research/04` and had not previously reached this layer.

### Human–AI combination is on average worse than the better single actor
*Sources:* [Vaccaro2024](REFERENCES.md#vaccaro2024)

Vaccaro et al. (2024) is cited in §2 as "not automatically synergistic". Stated fully: across 106 experiments, mean synergy relative to the better of human-alone and AI-alone was **negative** (Hedges' g ≈ −0.23), with losses concentrated in decision tasks. The optimistic reading — that design of the coupling is what matters — is an inference from the heterogeneity, not a finding.

### The mechanism this protocol relies on is disliked by the people it helps
*Sources:* [Bucinca2021](REFERENCES.md#bucinca2021)

Cognitive forcing reduced overreliance more than explainable-AI variants, and was rated **worse** by users (Buçinca et al. 2021). This protocol deliberately adds friction at high-consequence points. The evidence says that will work and be unpopular, which is a real adoption risk, not only a design trade-off.

### What follows honestly
The defensible headline is not "research supports this protocol". It is:

> **The closest study to this protocol's target task found no benefit from LLM support, and the broad meta-analysis finds average human–AI synergy negative. This protocol is a bet that the design of the interaction — not the presence of the AI — is what decides the outcome. That bet is plausible and unproven.**

Stating it that way is also what makes the project falsifiable, which is the point.

### What is not claimed here
None of this shows the protocol is wrong. Shin et al. tested particular LLM conditions, not this protocol; the meta-analysis predates most current models; the friction finding is about single decisions, not long-running discovery. The correct posture is neither dismissal nor deference: these are the results a serious critic will raise first, and the project should raise them itself.

---

## 3. Human Contribution Model

Current categories:

- Situated Grounding
- Framing & Meaning
- Independent Position / Authorship
- Judgment & Exceptions
- Commitment & Accountability

Research supports these better as **epistemic/normative roles** than as claims that humans are computationally superior.

Shared Language is cross-cutting rather than a sixth category.

---

## 4. Problem–solution result

The strongest synthesis remains:

> **Commitment late; probes early and reversible.**

The protocol should distinguish:

`Probe ≠ Candidate ≠ Recommendation ≠ Decision ≠ Commitment`

A probe should backpropagate learning into the problem/frame.

---

## 5. Shared-language result

The strongest refined claim is:

> **Meaning before commitment, not meaning before every name.**

Safe implications:

- AI may name early;
- model-bearing terminology begins as proposal;
- important human source meaning may need preservation;
- scenario/boundary use can test meaning;
- canonical language remains contextual and revisable;
- no full glossary is justified.

The exact lifecycle and explicit provenance UI remain experimental.

---

## 6. Evidence Case 02 method updates

The meta-retrospective identified process patterns that should influence the protocol:

### Criticism surfaces
Tentative models repeatedly triggered useful human correction.

### Framing authority
The human repeatedly corrected the level or object of the problem.

### Analogy boundary
Turn was useful but initially over-assimilated.

### Research model delta
Focused research changed the model materially.

### Explicit deferrals
Avoided premature technical lock-in.

### Structure has two modes
Exploratory structure and converged structure should not look/behave the same.

### Final baseline lacked one whole-package adversarial review
This should be added before stable/public release.

---

## 7. What remains weakly tested

- persistent external state;
- exact adaptive router;
- formal Human-first seed;
- explicit Probe label/debrief;
- formal concept terminology lifecycle;
- explicit source/provenance display;
- scenario gate;
- cold-start handoff quality of this protocol pack;
- predictive validity of evaluation metrics;
- portability across users/domains/harnesses.

---

## 8. Evidence relationship between Case 01 and Case 02

Case 02 was derived from Case 01's retrospective.

Therefore recurrence is:

> **cross-level dependent recurrence**

—not independent replication.

The next important evidence is a genuinely independent Case 03.

---

## 9. Public citation hygiene

The raw research reports (unpublished, see [`docs/provenance.md`](../docs/provenance.md)) carry internal citation markers of the tool that produced them. They remain discovery input, not public literature reviews.

Done on 22 September 2026: every source this file and `02` rely on was looked up again and is listed with a stable DOI or URL, marked peer-reviewed, preprint or practitioner, in [`REFERENCES.md`](REFERENCES.md). The same check located the claims in §2–§5 whose support is thinner than their wording; they are listed there and in [`docs/known-findings.md`](../docs/known-findings.md) (KF-3), not silently reworded.

Still open: reading the key papers in full rather than at abstract level, and re-checking the few fields marked unconfirmed in `REFERENCES.md`.
