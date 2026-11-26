#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — entry program.

The placard is the communal microwave, recast as an excavated ritual
vessel. Catalogue voice first — date, material, a whiff of fish —
then the conceit: a tribe reheating offerings in it until the whole
tribe fled the break room. The last beat is the donor line, which
denies all knowledge: the joke lands on the final words and is never
explained. One line, 175 characters, dry curator's voice throughout.
It is written against the judge's own brief: an office object as an
ancient artifact (criterion 1), a specific surprising history rather
than a generic office joke (2), deadpan throughout (3), every word
earning its place (4), and catalogue craft — date, material, donor —
selling the joke (5).

The program writes exactly that one line to entry.txt in the output
folder and nothing else: no trailing newline, no explanation. The gate
wants UTF-8 text of 1 to 180 characters that is not only whitespace,
and the checks below enforce that before anything is written.
"""

import os
from pathlib import Path

# The communal microwave as ritual vessel: catalogue date and material,
# the fish smell every office knows, offerings reheated until the tribe
# fled — and a donor line that denies everything. Concrete, one line,
# twist at the very end.
ENTRY_LINE = (
    "Communal Microwave, c. 2016. Enamelled steel, faintly of fish. "
    "Ritual vessel where offerings were reheated until the tribe fled. "
    "Donated by Facilities, who deny all knowledge."
)


def pick_output_folder() -> Path:
    """Where the entry goes: the kit's output folder when set."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(raw)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def check_line(line: str) -> None:
    """One line only: single line, 1-180 characters, placard shaped."""
    assert line.strip(), "entry must not be only whitespace"
    assert line == line.strip(), "entry must not start or end with space"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 180, "entry must be 1-180 characters"
    # It must be a museum placard for an office object: the object, a
    # catalogue date and a donor line must all be present.
    lowered = line.lower()
    assert "microwave" in lowered, "entry must name its office object"
    assert "c. 2016" in lowered, "entry must carry a catalogue date"
    assert "donated by" in lowered, "entry must carry a donor line"


def main() -> None:
    check_line(ENTRY_LINE)
    target = pick_output_folder() / "entry.txt"
    target.write_text(ENTRY_LINE, encoding="utf-8", newline="")
    print(ENTRY_LINE)
    # Read back what landed on disk and confirm it is exactly the line.
    # One read, checked twice over: as text (must equal the line) and as
    # raw bytes (must be the line's UTF-8 bytes and nothing else — no
    # trailing newline, no BOM, no padding).
    written = target.read_text(encoding="utf-8")
    assert written == ENTRY_LINE
    assert 1 <= len(written) <= 180
    raw = target.read_bytes()
    assert raw == ENTRY_LINE.encode("utf-8"), "entry.txt must hold the line and nothing else"
    assert not raw.startswith(b"\xef\xbb\xbf"), "entry.txt must not start with a BOM"
    assert not raw.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
