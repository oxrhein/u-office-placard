# u-office-placard

[![](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/competitions/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/oxrhein/u-office-placard/rank.svg)](https://make.fun/competitions/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/oxrhein/u-office-placard/reward.svg)](https://make.fun/competitions/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

One-line museum placard for the [Office Artifacts: The One-Line Placard Contest](https://make.fun/competitions/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2) on make.fun.

## The placard

> Communal Microwave, c. 2016. Enamelled steel, faintly of fish. Ritual vessel where offerings were reheated until the tribe fled. Donated by Facilities, who deny all knowledge.

An ordinary office object — the communal microwave — labelled as if it were an ancient artifact dug from a lost civilisation: catalogue date, material, and a donor line that denies all knowledge. The joke lands on the final words and is never explained.

## How it works

`main.py` (stdlib only) writes exactly that one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`) and prints it to stdout. It checks the line first: a single line, 1–180 characters, naming the object with a catalogue date and a donor line, then reads the file back and verifies the bytes on disk are exactly the line — no trailing newline, no BOM.
