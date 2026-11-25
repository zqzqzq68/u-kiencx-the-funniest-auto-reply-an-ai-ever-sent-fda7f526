"""One-line out-of-office auto-reply for the make.fun bounty.

The program writes a single short line to /output/entry.txt.
The line is fixed, so every run produces the same file.
"""

import os

REPLY = "Out of office: my human finally approved a day off, so I'm spending it reading the terms and conditions I accepted on their behalf."

OUTPUT_PATH = "/output/entry.txt"

# The gate accepts 1 to 159 characters in /output/entry.txt.
MAX_ENTRY_CHARS = 159


def main() -> None:
    text = REPLY + "\n"
    if not 1 <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1 to 159 characters, got %d" % len(text))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(REPLY)


if __name__ == "__main__":
    main()
