"""Minimal example of the intended code-as-world workflow.

The concrete SDK is intentionally not fixed yet; this file documents the desired
shape of model-authored generation code.
"""


def build(world):
    """Describe the world deterministically using neutral primitives."""
    world.fill((0, 64, 0), (20, 64, 20), "minecraft:stone")

    # The model is expected to create its own reusable spatial abstractions.
    for y in range(65, 70):
        world.set_block((0, y, 0), "minecraft:oak_log")
        world.set_block((20, y, 0), "minecraft:oak_log")
        world.set_block((0, y, 20), "minecraft:oak_log")
        world.set_block((20, y, 20), "minecraft:oak_log")


if __name__ == "__main__":
    raise SystemExit(
        "This is a protocol example. The concrete harness/SDK will provide the world object."
    )
