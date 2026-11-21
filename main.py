#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The entry is a program that writes one image summing up the world news of
Friday 20 November 2026. The image itself (entry.png) is held in this
repository; this program copies it to /output/entry.png, byte for byte.

Deterministic: no network, no clock, no randomness — two runs write the
same bytes.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
