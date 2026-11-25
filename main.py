"""Worst Superpower entry: writes the winning one-liner to /output/entry.txt."""
import os

ENTRY = "I can heat any doorknob I touch by exactly one degree, but only once a day."

def validate(entry):
    """Gate check mirroring the sealed scorer: 1-140 chars, one line, not blank."""
    assert entry == entry.strip(), "entry has leading/trailing whitespace"
    assert entry, "entry must not be empty or whitespace-only"
    assert 1 <= len(entry) <= 140, f"entry length {len(entry)} out of range"
    assert "\n" not in entry and "\r" not in entry, "entry must be exactly one line"
    return entry

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = validate(ENTRY.strip())
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Re-read and re-verify what actually landed on disk.
    written = open(path, encoding="utf-8").read()
    assert written == entry, "written file differs from validated entry"
    print(entry)
    print(f"chars: {len(entry)}")

if __name__ == "__main__":
    main()
