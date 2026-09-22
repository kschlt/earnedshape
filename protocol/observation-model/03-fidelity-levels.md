# Fidelity Levels

> **Status:** experimental, protocol v0.2. Rules may still change between versions.

> **Owns:** how well a run was observed, and which comparisons that permits.

Two surfaces will not be equally observable. Recording that difference is what keeps the evidence honest; ignoring it produces confident conclusions from incomparable data.

## The levels

| Level | Capture | Reliability | Typical surface |
|---|---|---|---|
| **auto** | the environment emits the event without the practitioner acting — hook, gate, file write | high; misses are defects and are detectable as `seq` gaps | a harness with deterministic hooks |
| **semi** | the model emits a structured record which something scripted collects | medium; the model may omit, embellish, or emit late | a surface with structured output but no hooks |
| **manual** | the practitioner records or exports by hand | low; biased toward what was memorable, and biased *in the direction of the hypothesis* | plain chat |

Fidelity is recorded twice: once per run (the dominant level) and once per event (`source`). The run-level value is the weakest level any required event kind reached.

## The bias that matters

Manual capture is not merely lossy, it is **systematically** lossy. A practitioner recording their own discovery remembers the moments where the method felt useful and forgets the ones where it was skipped. That is the exact direction that manufactures support for the hypothesis under test.

So: a manual run is legitimate evidence for *what happened when it happened*, and is not evidence about *how often* anything happened.

## Comparison rules

1. **Never compare frequencies across fidelity levels.** "Commitments were recorded more often with the capability active" is meaningless if one run was `auto` and the other `manual`.
2. **A baseline must be at least as well observed as the treatment.** A manual baseline against an auto treatment will show the treatment producing more of everything, because it was watched more closely.
3. **Every reported comparison names the fidelity of both sides.** If it cannot, it is not reportable.
4. **`semi` and `manual` runs may not carry a `capability.skipped` claim** unless `detected_by: analysis` and the analysis is reproducible from the record.
5. **A fidelity change mid-run splits the run**, or the run is recorded at the weaker level. Silent mixing is the one thing that makes a record actively misleading rather than merely thin.

## What this costs

Being strict here will make some intended comparisons impossible — most likely any Claude Code versus ChatGPT comparison of how often something happened. That is a real loss, and it is better than the alternative, which is a comparison that looks rigorous and is not. <!-- lint:vendor-ok -->

It also produces a useful design pressure: if a hypothesis can only be tested at `auto` fidelity, then it can only be tested in a surface with hooks, and that belongs in the surface fitness recommendation rather than being discovered late.
