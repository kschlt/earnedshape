# Phase 1 — what can be observed, before anything is steered

> **Status (22 September 2026):** planned; one instrument built, no spike run yet.
> **Purpose:** fill [`capabilities/CONFORMANCE.md`](../capabilities/CONFORMANCE.md) and its event-reachability table with **demonstrations, demonstrated impossibilities or named costs**, never opinions.

## Why this comes first

The protocol makes claims about what happens in a discovery: a provisional model draws more correction than a polished one, a recorded commitment survives a session boundary, a challenge changes a decision. None of these can be evaluated unless the events they depend on can be recorded. So the order is fixed:

1. find out what each environment lets you **observe**;
2. record one baseline discovery with **every steering capability switched off**;
3. only then introduce steering capabilities, one at a time, each against that baseline.

A capability built before step 1 might be unmeasurable. A steering capability built before step 2 leaves nothing to compare against, and the baseline cannot be reconstructed afterwards.

## Rules for the spikes

1. **Spike code is throwaway.** Nothing written for a spike goes into an adapter. A spike that turns into the implementation skips the design step it exists to inform.
2. **One question per spike**, answerable in a sitting.
3. **A negative result is a result.** "Not reachable" fills a cell and demotes a hypothesis, which is worth more than a hurried workaround.
4. **Record cost, not just possibility.** "Reachable, but needs a hosted endpoint" is a different answer from "reachable".
5. **No content leaves the spike.** [`04-recording-boundaries.md`](../protocol/observation-model/04-recording-boundaries.md) applies from the first captured byte.

## The spikes

| | Question | Status |
|---|---|---|
| **S-0** | Which ChatGPT surface is the second environment: plain chat, a Project, or a Custom GPT with Actions? An owner decision, not a spike; it shapes S-6 to S-8. | open |
| **S-1** | **Is a conversational turn observable** without the model being asked to report it? Decisive: without it, the criticism-surface hypothesis (`HYP-001`) and turn economics (`HYP-009`) are unmeasurable here and get demoted in writing. | **instrument built and self-tested; run pending** |
| S-2 | Does state written in one session arrive intact in the next, across three boundaries including a compaction? (`CAP-01`) | planned |
| S-3 | Can "capability available" be told apart from "capability used", and can a skip be detected? Without this, evaluation level 1 does not exist. | planned |
| S-4 | What does enforcement cost? The same short discovery three times, for the commitment act (`CAP-04`) as guidance, as a skill, and as a deterministic gate, comparing compliance and interruptions. This is the only chance to measure compliance before hardening removes the signal. | planned |
| S-5 | Can "observe this session, ignore that one" be made reliable and fail-open? | planned |
| S-6 | On the chosen ChatGPT surface: per event kind, is capture automatic, semi-automatic, manual, or impossible? | after S-0 |
| S-7 | If the model is asked to emit structured records, how often does it omit, invent or emit late, compared with a manual log over 30 turns? | after S-0 |
| S-8 | What enforcement level is reachable without hooks? Feeds a recommendation on which discoveries belong in which environment. | after S-0 |
| S-9 | One short real discovery, observation only, producing a complete run record: the baseline. | after S-1 to S-5 |

Sequencing: S-1 first and alone, because a negative result changes the observation model before anything is built on it. S-2 to S-5 in any order. S-9 last, once the record format has settled; a baseline recorded in a format that then changes is not a baseline.

## S-1 in more detail

The instrument is a set of hook scripts for Claude Code (kept in the private working repository, as throwaway spike code). It records one line per hook event — timestamp, event name, session id, the **names** of the payload fields, a length bucket for the human's text — and never any text or value. It prints nothing, because anything a hook prints at a prompt boundary is injected into the model's context, and an instrument that talks changes the conversation it measures. It fails open on every path.

Two findings came out of building it, before any run:

- **An interrupted turn and a dropped event leave the same trace.** The stop event does not fire on a user interrupt. So the analysis has three verdicts, not two: *clean*; *explained*, where the only gaps are unanswered human turns and the human checks the count against how often they actually interrupted; and *refused*. The two-verdict version passed a dropped turn in the self-test, which is how the third verdict was found.
- **Recording payload keys rather than assuming them** means the first run reports the harness's actual contract instead of the author's expectation.

What the run needs: a real conversation of at least 20 exchanges, with tool use, at least one interruption, and ideally long enough to compact. The case that matters most is not in any verdict: whether the stream survives compaction and long sessions, because a discovery is long by definition.

## Exit

Phase 1 is done when every cell in the conformance matrix and the event-reachability table holds a demonstration, a demonstrated impossibility or a named cost; when there is a recommendation on which discoveries belong in which environment; and when every hypothesis that turns out unobservable everywhere has been marked as such in the protocol instead of looking like a mechanism awaiting evidence.
