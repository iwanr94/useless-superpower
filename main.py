"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single line (at most 200 characters) naming a hilariously
useless superpower to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "I can summon any object I've ever lost - but it only shows up "
    "three days after I've already bought a replacement."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
