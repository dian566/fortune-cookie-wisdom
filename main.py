"""Entry for the make.fun one-line bounty: fortune-cookie wisdom for developers.

Writes the single-line entry (max 120 characters) to /output/entry.txt.
"""

import os

LINE = "The meeting that could have been an email will outlive the code it discussed."

assert LINE, "entry line must not be empty"
assert len(LINE) <= 120, f"entry line is {len(LINE)} characters, over the 120-character limit"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
