# Evaluation & Learning Protocol v0.2

## 1. Principle

The protocol itself is a versioned hypothesis.

Evaluate:

- discovery quality;
- human understanding/agency;
- state integrity;
- convergence quality;
- downstream handoff fitness;
- active human effort.

Do not optimize one composite score.

---

## 2. Quality gates + Pareto comparison

### Gate 1
Discovery/handoff quality must remain acceptable.

### Gate 2
Human understanding/agency must not materially deteriorate.

Then compare:
- state integrity;
- convergence;
- workload;
- active human time;
- process overhead.

A faster protocol is not better if it produces more product rediscovery or weaker human ownership.

---

## 3. Core run-level signals

### Cold-Start Handoff Blockers
Can a fresh implementation context proceed using only the final discovery baseline?

### Decision Explainability Coverage
Can the human explain consequential decisions, alternatives, trade-offs and uncertainty without the original AI?

### State-Integrity Defects
Lost decisions, contradictions, stale assumptions, missing provenance/status.

### Useful Breadth before Commitment
Materially distinct frames/solution mechanisms considered before high-impact commitment.

### No-New-Evidence Reopenings
High-impact decisions reopened without meaningful new evidence, constraint, user information or error discovery.

### Active Human Time
Human work time separated from AI latency/calendar time.

### Workload / Agency Pulse
Short self-report.

---

## 4. Shared-language diagnostic signals

These are **experimental**, not core success metrics.

Potential observations:

### Late Concept Disagreement
A term previously treated as stable later reveals materially different meanings.

### High-impact Late Rename
A late rename/split changes downstream requirements, decisions or boundaries.

### Scenario Agreement
Human and AI independently classify new cases consistently under a shared concept.

### Independent Human Explanation
Can the human explain the concept and its boundary without copying AI wording?

### Source-Recovery Value
Did preserved source language later reveal a semantic drift or hidden intent?

### Terminology Burden
How much interaction/state overhead does explicit terminology management create?

Do **not** optimize:
- number of AI-originated terms;
- raw renaming rate;
- lexical alignment.

Those measures are ambiguous.

---

## 5. Research Model Delta

After research:

```text
Previous model
→ Evidence
→ REINFORCED / REFINED / CHALLENGED / NEW / NO CHANGE
→ decision impact
→ remaining uncertainty
```

Research quality should partly be judged by whether it resolves a meaningful uncertainty or changes the working model.

---

## 6. Short AAR

After each completed discovery:

1. Which 1–3 decisions were consequential?
2. Which can I explain and defend without the original dialog?
3. Where did AI meaningfully improve my model?
4. Where did I nearly accept AI too easily?
5. Which perspective/constraint/counterhypothesis arrived late?
6. Which iteration was unnecessary?
7. Which important concept/term was misunderstood, renamed or silently stabilized?
8. What one protocol change might have had the largest effect?

---

## 7. Protocol change template

```text
Observation:
Hypothesis:
Mechanism:
Expected effect:
Possible side effect:
Measures:
Decision rule:
```

---

## 8. Learning loop

```text
real run
→ mostly automatic measurement
→ short AAR
→ protocol hypothesis
→ small change
→ several runs
→ pattern review
→ controlled comparison if needed
```

---

## 9. Keep / Investigate / Revert

### Keep
Quality stable/improving; agency stable; defects/effort improve.

### Investigate
Efficiency improves but breadth, understanding, defective-AI resistance or semantic consistency declines.

### Revert
Major blockers, discovery reopenings, understanding loss or systematic state/concept defects increase.

---

## 10. Priority experiments from v0.2

### E1 — Criticism Surface
Incomplete working model vs polished model.

### E2 — Human-first Signal
Selective independent human articulation before strong AI anchor.

### E3 — Solution Probe + Debrief
Explicit probe lifecycle vs natural reflection.

### E4 — External Runtime State
Persistent state vs conversation-only reconstruction.

### E5 — Candidate-first Terminology
Candidate language vs silent canonicalization.

### E6 — Meaning-first selective terminology
Semantic probe → candidate → use-test for high-impact concepts.

### E7 — Source-preserving reformulation
Original phrase retained beside AI interpretation vs replacement.

### E8 — Analogy Boundary Check
Explicit non-transferability analysis vs analogy-only reuse.

### E9 — Exploration-turn brevity
Compact navigation turns vs repeated long synthesis.

### E10 — Bounded uncertainty readiness
Handoff with explicit technical deferrals vs more exhaustive discovery.

---

## 11. Independent Evidence Case 03

The next major evidence milestone should be a content-independent case.

Preferably instrument it **before** the discovery begins:

- protocol version;
- model/harness version;
- active state mechanism;
- selected hypotheses;
- lightweight telemetry;
- AAR;
- planned cold-start handoff test.

The goal is to move from retrospective inference toward prospective evidence.
