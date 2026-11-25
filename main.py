"""Hand the judge one spectacularly bad money tip, delivered deadpan.

The bounty asks for the worst advice an AI could give, judged in blind
Swiss rounds by a deadpan comedy critic who compares two entries at a
time and stops at the first real difference. The winning shape here is a
tip that sounds thrifty and confident while quietly gambling everything:
drop the insurance, trust careful driving alone, and call that the whole
trick — the gamble is the joke, and the straight face is what sells it.
One sentence, no hedging, no wink — the danger has to dawn on the
reader a beat after the punchline lands.

The entry is capped at 140 code points and this line runs 116, so the
program below does nothing clever at all: it checks the length, writes
the fixed sentence to the exact path the bounty demands, and leaves the
bytes identical on every run. No network, no randomness, no arguments.
"""

import os

WORST_ADVICE = "To save money, cancel your insurance and just drive carefully. Careful drivers never crash — that's the whole trick."

# The bounty caps an entry at 140 code points; this sentence is 116, so
# the guard below has real headroom and only fires if someone edits the
# advice itself. A rejected length must crash loudly rather than emit a
# file the scorer would refuse to grade — a silent bad file is worse
# than no file at all, because it burns a submission slot.
ADVICE_FLOOR_CODE_POINTS = 1
ADVICE_CEILING_CODE_POINTS = 140

# The bounty names this exact destination; the judge only ever reads the
# file that lands here, so the path is a constant, never a guess.
ENTRY_DIRECTORY = "/output"
ENTRY_PATH = "/output/entry.txt"


def write_worst_advice() -> None:
    """Write the fixed advice line to the entry file, byte for byte."""
    advice_length = len(WORST_ADVICE)
    if not ADVICE_FLOOR_CODE_POINTS <= advice_length <= ADVICE_CEILING_CODE_POINTS:
        raise ValueError(
            "worst advice must stay within 1 to 140 code points, "
            f"but this draft runs {advice_length}"
        )
    os.makedirs(ENTRY_DIRECTORY, exist_ok=True)
    try:
        os.chmod(ENTRY_DIRECTORY, 0o755)
    except OSError:
        pass
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(WORST_ADVICE)
    os.chmod(ENTRY_PATH, 0o644)


if __name__ == "__main__":
    write_worst_advice()
