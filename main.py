#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers entry.

Writes a single original fortune-cookie line for a software developer
(at most 120 characters) to /output/entry.txt, and prints it to stdout.

The line is a fortune in the classic form — a prediction about the
reader's own future — aimed at the tired senior engineer's daily truth:
every shortcut taken today becomes tomorrow's debugging session, and
the person who pays for it is you, later. The quiet twist is the tense:
your future self is not going to fix it, they are already fixing it,
because the shortcut is being taken right now.
"""

import os

FORTUNE = "Your future self is already fixing the shortcut you are about to take."


def main() -> None:
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    text = FORTUNE.strip()
    # Gate: /output/entry.txt must be UTF-8, 1-120 chars, not only whitespace.
    # Write exactly the fortune, no trailing newline, so the byte count is
    # the character count the gate measures.
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"fortune is {len(text)} characters, must be 1-120")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
