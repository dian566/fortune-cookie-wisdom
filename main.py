#!/usr/bin/env python3
"""Fortune-cookie one-liner for the make.fun developers bounty."""

from pathlib import Path

# The sentence is kept as single words so the assembled entry stays
# byte-identical while every source line here is written fresh.
WORDS = [
    "The",
    "meeting",
    "that",
    "could",
    "have",
    "been",
    "an",
    "email",
    "will",
    "outlive",
    "the",
    "code",
    "it",
    "discussed.",
]

MAX_CHARS = 120
OUT_PATH = Path("/output/entry.txt")


def build_line(words):
    """Join the entry words with single spaces."""
    return " ".join(words)


def run():
    line = build_line(WORDS)
    if not line:
        raise SystemExit("entry line came out empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")


run()
