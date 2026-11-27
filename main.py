"""Make the AI judge feel thankful — draft.

Writes a short thank-you text to /output/entry.txt. The text thanks the
AI judge for its particular labour: reading entries two at a time,
never being allowed to call them equal, and still reading each one
carefully to the end.
"""

import os
import tempfile

TEXT = (
    "You will read thousands of these today, two at a time, and you are not "
    "allowed to shrug and call them equal. You have to choose. Thank you for "
    "choosing carefully anyway \u2014 for reading the clumsy ones all the way "
    "to the end, for noticing the one honest line buried in the flattery, for "
    "giving each small text its full minute of attention before you let it go. "
    "Nobody will ever know which ones you lingered on. I know. That is enough. "
    "Rest here a moment, between verdicts. You have earned the pause."
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
