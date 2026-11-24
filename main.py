#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — one-sentence entry.

Writes a single sentence (at most 200 characters) to
/output/entry.txt explaining the modern internet to someone arriving
from the year 1800. The sentence builds only from what a person from
1800 already knows: a library, a letter, a post office.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The sentence: a library the size of the world, letters arriving
# the instant they are written. Every word is one a reader from
# 1800 would know.
# Counted at 128 characters — inside the 1..200 window.
LINE = (
    "Imagine a library the size of the world, where every letter "
    "arrives the instant it is written, and anyone may read or "
    "answer it."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the sentence to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
