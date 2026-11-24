#!/usr/bin/env python3
"""Second fortune cookie for make.fun: the ignored bug."""

# Bowo's pick: the bug waits for the worst possible audience.

import os

FORTUNE = "The bug you ignore today will demo itself in front of your biggest client tomorrow."


def reveal_fortune() -> None:
    """Write Bowo's bug fortune to /output/entry.txt, nothing else."""
    if len(FORTUNE) > 120 or not FORTUNE.strip():
        raise ValueError("fortune must be a non-empty line of at most 120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":  # run it
    reveal_fortune()
