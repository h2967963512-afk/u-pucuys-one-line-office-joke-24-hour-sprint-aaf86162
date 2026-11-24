"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line about office life: a meeting becomes an
# email, the email gets a meeting, and the email requests a follow-up.
# The setup escalates and the punch lands on the last few words.
# One sentence, 133 characters — inside the 200-character gate.
# Revision note: wording kept as first drafted; no change to the entry
# text itself, which was verified byte-identical to the intended line.
import os

TEXT = (
    "We moved the meeting to an email, then scheduled a meeting to "
    "discuss the email, and now the email has requested a follow-up "
    "meeting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
