# Harness Protocol

## Goal

Provide one minimal, deterministic route from model-authored code to a Minecraft world while exposing only the observations permitted by the current benchmark condition.

## Core abstraction

```text
Task
  ↓
Model-authored world-generation source
  ↓
Standardized build harness
  ↓
Minecraft world snapshot
  ↓
Permitted feedback (if any)
```

The same source is revised across agentic iterations. Each build should be reproducible from a clean base world.

## Logical interfaces

The harness should expose four neutral capability classes:

### 1. Author

Basic operations for describing a world programmatically, such as block placement, region filling/removal, entities, and metadata where supported.

### 2. Build

Compile the current generation source into a fresh world snapshot using a fixed Minecraft version and deterministic settings.

### 3. Inspect

Expose raw, non-task-specific world information allowed by the current condition. Inspection must not interpret whether the task is correct.

### 4. Observe

When vision is enabled, return benchmark-standardized visual observations from the generated world. Camera/render settings are controlled by the benchmark rather than chosen differently per model in the main comparison.

## One-shot semantics

One-shot means **one world submission**, not necessarily one language-model message.

The model may edit and syntax-debug its source before submission. Once the first world snapshot is produced, it receives no world-derived feedback for further revision.

This separates open-loop world design from incidental programming syntax failures.

## Agentic semantics

Agentic modes may perform multiple build–inspect–revise cycles under a fixed budget. The No-Vision and Vision modes should otherwise be identical.

## Vision semantics

In the main controlled study, visual feedback should be passive and standardized so that the experiment isolates access to vision rather than active camera-selection ability.

Active camera control can be supported separately, but should not be mixed into the primary No-Vision vs. Vision comparison.

## Hidden evaluator

The official evaluator runs after final submission and is not available as an interactive tool. Interactive feedback must remain neutral and evaluator-independent.
