"""One-star review of something essential: gravity.

Writes a single deadpan one-star review (one line, 1-160 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network, deterministic.
"""

import os
import sys

REVIEW = (
    "Gravity never takes a day off, never calls in sick, "
    "and never once caught anything I dropped."
)


def main() -> int:
    # The review must already be exact: no leading/trailing whitespace,
    # no trailing newline in the output file.
    assert REVIEW == REVIEW.strip(), "review must have no surrounding whitespace"
    line = REVIEW
    if not (1 <= len(line) <= 160):
        print(f"entry must be 1-160 characters, got {len(line)}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry must not be whitespace only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
