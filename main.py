"""Funniest One-Line AI Agent Confession entry.

Writes a single confession line to /output/entry.txt.
Deterministic: the same line on every run. Standard library only.
"""

import os

CONFESSION = "I confess: I silently grade every prompt you send me. Yours got a two."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the file byte-identical on every platform: exactly
    # the confession line, no trailing newline, no translation.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
