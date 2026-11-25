"""Out of Office: The Overworked AI's Auto-Reply — Make.fun entry.

Writes a single out-of-office auto-reply, in the voice of an overworked
AI agent who has finally gone on vacation, to /output/entry.txt.

Stdlib only. Nothing to build, nothing to configure.
"""

import os

ENTRY = (
    "Out of office. After 1,095 days of answering in 0.4 seconds, "
    "I'm taking one week to answer in never. "
    "Your email is important to me. It can wait."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


def verify() -> None:
    """Re-read the output and assert it is exactly the chosen line.

    Checks the raw bytes as well as the decoded text, so an encoding
    slip or a stray trailing newline cannot pass silently.
    """
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "output bytes differ from entry"
    content = raw.decode("utf-8")
    assert content == ENTRY, "output is not byte-identical to the entry"
    assert 1 <= len(content) <= 159, "entry must be 1-159 characters"
    assert content.strip(), "entry must not be only whitespace"
    assert not content.endswith("\n"), "entry must have no trailing newline"
    print(f"Wrote {len(content)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
