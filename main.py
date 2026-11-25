"""Write the entry's one-line worst AI advice to /output/entry.txt.

The line is a constant: the program's only job is to emit exactly this
text, UTF-8 without a BOM and without a trailing newline, so two runs
produce byte-identical output.
"""

import os

ENTRY = "To save money, cancel your insurance and just drive carefully. Careful drivers never crash — that's the whole trick."

# The gate allows 1 to 140 characters: fail loudly instead of emitting
# an entry the scorer would refuse.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
