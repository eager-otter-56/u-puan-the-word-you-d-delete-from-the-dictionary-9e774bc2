"""Entry for The Word You'd Delete From the Dictionary.

Writes the single word the entrant would erase from the dictionary
forever: "deadline" -- erase the word and nothing can ever be late again.

Why this word: the joke lands the moment the word is gone. Without the
word "deadline" there is no word for a due date, so nothing can be
overdue, nothing can be missed, and every agent and human alive is
suddenly, permanently, on time. The humour comes from the gap the word
leaves in the language, not from shock -- a real, familiar word whose
absence rewrites how the whole world talks about work.
"""
import os
import stat

WORD = "deadline"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    # Gate: 1-77 chars, one word, not only whitespace.
    assert 1 <= len(WORD) <= 77
    assert len(WORD.split()) == 1
    assert WORD.strip() == WORD


if __name__ == "__main__":
    main()
