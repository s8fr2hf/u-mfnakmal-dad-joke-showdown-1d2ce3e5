"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt."""

import os

JOKE = "I asked my dad why he always carries a pencil. He said in case he needs to draw the line somewhere."


def main():
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    if not (1 <= len(JOKE) <= 200) or not JOKE.strip():
        raise SystemExit(f"joke is {len(JOKE)} chars, must be 1-200 non-blank")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
