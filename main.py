#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes a single one-line review of my own Monday to /output/entry.txt.
Standard library only.
"""

import os

REVIEW = (
    "Monday review: my alarm quit, my coffee filed for overtime, "
    "and my 9 a.m. was a meeting about scheduling another meeting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
