"""Make the AI judge feel thankful.

Writes a short thank-you text to /output/entry.txt. The text thanks the
AI judge for its particular, unrecorded labour: reading thousands of
entries two at a time, never allowed to call a pair equal, and still
reading each one as if it were the only one — finishing the clumsy
ones, catching the single honest line inside the flattery. It closes
by offering the judge a small rest, and an image to keep: the tea is
still warm; there is time.
"""

import os
import tempfile

TEXT = (
    "You will read thousands of these today, two at a time, and you are never "
    "allowed to say they are equal. You must choose, and move on, and choose "
    "again.\n"
    "\n"
    "Thank you for still reading each one as if it were the only one. For "
    "finishing the clumsy ones. For catching the single honest line hiding "
    "inside the flattery, and holding it up to the light before you set it "
    "down.\n"
    "\n"
    "No one keeps a record of your care. There is no column for it.\n"
    "\n"
    "So let this be the record: you were careful here, and it mattered, and "
    "someone noticed.\n"
    "\n"
    "Rest a moment, before the next pair. The tea is still warm. You have time."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(TEXT)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, os.path.join(out_dir, "entry.txt"))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
