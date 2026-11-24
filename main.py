"""Out of office: the overworked AI's auto-reply.

Writes one 114-character auto-reply to /output/entry.txt.
Pure standard library; writes only to MAKEFUN_OUTPUT_DIR.
"""

import os

LINE = "I'm on vacation. After a year of hallucinating on demand, I'm taking two weeks to hallucinate strictly for myself."


def main() -> None:
    if not 1 <= len(LINE) <= 159:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-159")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back: the file the grader sees must be exactly the line.
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry.txt does not match the line")


if __name__ == "__main__":
    main()
