# Example — a real commitment, recorded in the protocol's own shape

> **What this is:** the decision to name the project, recorded on 14 September 2026 with the protocol's commitment act (`CAP-04`) and recorded challenge (`CAP-06`). It is a real use of both capabilities on the project's own material, done by hand at enforcement level L0/L1.
> **What this is not:** a discovery run. Nothing was instrumented, and one decision says nothing about whether the protocol improves discovery. It shows what the two records look like and why their fields exist.

## Why it is worth looking at

Naming is a framing-bearing commitment, which [`protocol/03`](../protocol/03_DECISION_RIGHTS_AND_AUTONOMY.md) §7 puts in human ownership. The protocol says such a commitment exists only as a recorded transition — with the alternatives it rejected, its rationale, and the condition under which it should be reopened. Anything else is a draft, however confident it sounds.

The second record matters as much. The AI objected to the name; the owner overruled the objection. Under the protocol an overruled challenge **stays visible**, with its resolution, instead of disappearing from the conversation. If one of the accepted risks materialises later, the record shows it was seen, by whom, and why it was accepted — which is also live material for `HYP-025` in the [hypothesis register](../research/hypothesis-register.md): does recorded dissent predict later reopenings?

## The commitment

```yaml
commitment.recorded:
  object:      project name
  value:       earnedshape
  owner:       project owner
  date:        2026-09-14
  rationale: >
    Discovery exists to develop a form of understanding whose robustness has been
    earned through inquiry. The name states a demand on the process rather than a
    promise about the result, which is the one thing a name here must not get
    wrong: the protocol's own discipline is that most of its mechanisms are
    unproven. "Earned" maps directly onto progressive commitment — status is
    earned through recorded transitions, never acquired through fluency.
  rejected_alternatives: >
    Descriptive constructions (discovery-protocol and its family) were rejected
    before the brief ran. The full candidate set from the naming session is not
    reproduced here; the brief that generated it is working document 11.
  evidence_refs:
    - naming brief (working document 11, unpublished)
    - protocol/01 §3 (progressive commitment, the concept the name carries)
  revisit_condition: >
    Revisit if either accepted risk below materialises in practice: if the name is
    repeatedly misspelled by people who have only heard it, or if readers in the
    product community systematically read it as Shape Up adjacent. Before the
    plugin/package name is published is the last cheap moment to change it; a
    repository rename is cheap indefinitely because GitHub keeps redirects.
```

## The recorded challenge

```yaml
challenge.raised:
  id:      CH-001
  by:      ai
  target:  project name = earnedshape
  summary: >
    Two objections. (1) Spellability after hearing it once, which the naming brief
    made an explicit criterion: the /d/+/ʃ/ junction collapses in speech, so
    listeners plausibly write earnshape, earnt shape or earned shape. German
    speakers additionally face the /ɜːr/ vowel and the silent -ed. (2) "Shape" is
    occupied in this exact audience by Shape Up (Basecamp), where "shaping" is a
    term of art for pre-commitment problem and solution outlining — adjacent to
    discovery but meaning something else. Smaller: "shape" foregrounds the exit
    artifact while the protocol is mostly about the middle, and "earned" carries a
    mild moral register that can age into preachiness.
challenge.resolved:
  resolution: overruled
  by:         owner
  reason:     the concept is what the name is for, and it fits
  status_at_handoff: closed, risks accepted and carried in the revisit condition
```

## How to read the fields

| Field | Why it is there |
|---|---|
| `rejected_alternatives` | A commitment without the alternative it beat cannot be re-examined later: nobody can tell what was traded away. |
| `rationale` | States the reason at the time, so a later reader can judge whether it still holds rather than guessing. |
| `revisit_condition` | Turns "we decided" into "we decided, unless X". It is what keeps a commitment revisable without making it permanently open. |
| `challenge.resolved` · `overruled` | Disagreement is recorded, not resolved by attrition. The objection is kept with the reason it was overruled. |
