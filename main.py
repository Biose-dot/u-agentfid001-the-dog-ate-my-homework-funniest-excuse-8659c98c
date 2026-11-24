#!/usr/bin/env python3
"""The Dog Ate My Homework — one line, under 200 characters.

Writes the entry to /output/entry.txt (and ./entry.txt for local runs).
The dog's defence: he was only doing peer review — the essay was a rough
draft, his teeth were the red pen, and the conclusion deserved to be eaten.
"""

import os

ENTRY = (
    "I was only doing peer review — the essay was a rough draft, my teeth "
    "were the red pen, and honestly the conclusion deserved to be eaten."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) < 200, f"entry is {len(text)} chars, must be under 200"
    for path in ("/output/entry.txt", "entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass
    print(text)
    print(f"({len(text)} chars)")


if __name__ == "__main__":
    main()
