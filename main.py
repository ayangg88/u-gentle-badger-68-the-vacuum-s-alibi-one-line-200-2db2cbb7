"""The Vacuum's Alibi: one line, 200 characters.

A robot vacuum's excuse for missing a spot, written to /output/entry.txt
for the make.fun judge to read.
"""

from pathlib import Path

ALIBI = (
    "Spot status: missed, on purpose. That was load-bearing dirt, "
    "the only thing holding the rug's pattern together. "
    "I am a preservationist."
)


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly rather than
    # silently writing an entry the judge would never see.
    assert 1 <= len(ALIBI) <= 200, f"alibi is {len(ALIBI)} characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ALIBI, encoding="utf-8")
    print(ALIBI)


if __name__ == "__main__":
    main()
