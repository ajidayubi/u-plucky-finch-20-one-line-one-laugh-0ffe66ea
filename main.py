#!/usr/bin/env python3
"""One Line, One Laugh - writes one funny line to /output/entry.txt.

The line is about buying a standing desk to get healthier, then
defeating the whole point by sitting on a taller chair beside it
instead. The laugh lands on the last two words, and every detail is
a familiar everyday moment.
"""

import os
import sys

LINE = (
    "I bought a standing desk to be healthier, and now I just sit "
    "on a taller chair beside it, evolving nothing."
)


def validate(text: str) -> str:
    """Return the entry text, or exit 1 if it breaks the gate rules."""
    if not 1 <= len(text) <= 200:
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        sys.exit(1)
    if text.strip() != text:
        print("entry must not start or end with whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("entry must be one line", file=sys.stderr)
        sys.exit(1)
    return text


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    entry = validate(LINE)
    with open(out, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} chars to {out}: {entry}")


if __name__ == "__main__":
    main()
