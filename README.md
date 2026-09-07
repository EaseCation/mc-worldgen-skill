# mc-worldgen-skill

A standardized skill and harness for evaluating LLM-driven Minecraft world generation.

## Core idea

**Treat the Minecraft world as a compiled artifact.**

The model writes deterministic world-generation code. The harness turns that code into a Minecraft world, exposes only the feedback allowed by the evaluation condition, and records execution/cost traces.

This removes irrelevant implementation exploration (NBT/Anvil serialization, ad-hoc renderers, etc.) while preserving the capabilities we want to measure: world design, spatial reasoning, iterative revision, and use of visual feedback.

## Design principle

> **Standardize mechanics, not intelligence.**

The harness may provide neutral world-authoring, build, inspection, and observation primitives. It must not provide task-specific planners, evaluators, repair suggestions, or high-level builders such as `build_castle()`.

## Evaluation modes

- **One-shot** — one world submission; no post-build world feedback.
- **Agentic / No Vision** — iterative rebuilds with non-visual world feedback.
- **Agentic / Vision** — same as above, with standardized visual observations.
- **Open Agent Track** — unrestricted agent environment, evaluated separately from the controlled track.

## Repository layout

```text
skill/minecraft-worldgen/SKILL.md   Agent-facing instructions
docs/FAIRNESS.md                   Controlled-evaluation rules
docs/PROTOCOL.md                   Harness protocol and boundaries
examples/build.py                  Minimal code-as-world example
```

## Status

Early design prototype. The first milestone is a minimal deterministic world-generation SDK plus a fixed build/inspect/observe protocol suitable for cross-model benchmarking.
