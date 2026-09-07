# Minecraft World Generation Skill

Use this skill when the task is to create or revise a Minecraft world for the controlled benchmark.

## Mental model

Treat the Minecraft world as a **compiled artifact**.

Your source of truth is deterministic world-generation code. Do not manually author Minecraft region/NBT files and do not spend time inventing a new serialization pipeline. Express the design in code, build the world through the provided harness, inspect only the feedback available in the current evaluation mode, revise the same source, and rebuild.

## Required workflow

1. Read the task requirements.
2. Plan the world in coordinates, regions, structures, and materials.
3. Implement the design as deterministic generation code.
4. Build through the provided harness.
5. If the current mode permits feedback, inspect the permitted feedback and revise the same generation source.
6. Submit the final reproducible build.

## What you should do yourself

You are responsible for:

- spatial planning;
- layout and coordinate reasoning;
- structure and detail design;
- choosing materials;
- interpreting task constraints;
- deciding what to revise;
- using visual feedback when available.

## What the harness is responsible for

The harness standardizes:

- Minecraft world serialization and version details;
- deterministic world rebuilding;
- neutral world-authoring primitives;
- neutral state inspection;
- standardized visual observations when enabled;
- execution logging and resource accounting.

## Prohibited shortcuts

Do not expect or request task-specific helpers such as:

- `build_house()` / `build_castle()`;
- `fix_design()`;
- `check_task_completion()`;
- `find_missing_windows()`;
- `make_symmetric()`;
- evaluator scores or hidden requirement diagnostics.

The harness standardizes mechanics, not task intelligence.

## Evaluation modes

### One-shot

You may author and syntax-debug the generation source, then produce one world submission. After the world is built, no world-state or visual feedback is available for revision.

### Agentic / No Vision

You may rebuild repeatedly and inspect permitted non-visual world state between revisions. No image observations are available.

### Agentic / Vision

The same iterative workflow is available, with standardized visual observations in addition to the same non-visual feedback.

### Open Agent Track

This skill does not constrain the open track. Open-track agents may choose their own engineering approach; those results are reported separately from controlled model comparisons.

## Reproducibility rule

The final world must be reproducible from a clean base world using the submitted generation source. The generated world itself is an output artifact, not the canonical source.