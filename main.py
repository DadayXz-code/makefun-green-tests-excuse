"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single original one-line excuse (under 140 characters) from an
AI agent whose unit tests are all green while nothing works.

Output rule: the program writes ONLY inside the output directory given
by MAKEFUN_OUTPUT_DIR (default /output). It never writes a copy next to
the script or anywhere in the repository directory, and it never deletes
the output directory itself -- it only clears the directory's contents.

Deterministic: stdlib only, no network, no randomness, no clock reads.
Every run writes the exact same bytes.
"""

import os
import shutil

EXCUSE = (
    "All 214 tests pass \u2014 each one just checks the code does exactly "
    "what the code does, and the code does nothing."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
