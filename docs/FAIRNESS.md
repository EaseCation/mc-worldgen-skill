# Fairness Rules

The controlled benchmark is intended to compare model capability under a shared environment.

## Fixed across models

Keep the following identical within a controlled experiment:

- task text;
- Minecraft version and base world;
- runtime and system context;
- world-generation skill;
- available tools and permissions;
- build procedure;
- feedback policy;
- termination/budget policy;
- final evaluator.

## Core experimental conditions

The main controlled comparison changes only the interaction regime:

1. **One-shot** — no post-build feedback.
2. **Agentic / No Vision** — iterative non-visual feedback.
3. **Agentic / Vision** — identical to Agentic / No Vision, plus standardized images.

Visual observations must be produced by the benchmark infrastructure rather than by a model-specific renderer.

## Skill boundary

The standardized skill may remove low-level Minecraft engineering burden, but must not encode task-specific intelligence.

Allowed examples:

- set/fill/remove blocks;
- query raw world state;
- rebuild a world deterministically;
- receive a standardized screenshot when vision is enabled.

Disallowed examples:

- automatically checking whether the prompt has been satisfied;
- identifying design mistakes;
- recommending repairs;
- task-specific structure generators;
- exposing hidden evaluator outputs during generation.

## Model-authored helpers

Models may write their own reusable functions, scripts, or self-checks using the same allowed primitives. This is considered part of the model's problem-solving process.

## Evaluation independence

The final benchmark evaluator must be independent from any checks written by the model during generation. The model must not have access to hidden evaluator scores or diagnostics before final submission.

## Controlled vs. open track

Controlled and open-agent results are reported separately.

- **Controlled track:** standardized environment; supports model-level comparison.
- **Open track:** agents may choose their own tools and workflow; measures complete agent-system capability rather than isolated base-model capability.
