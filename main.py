#!/usr/bin/env python3
"""Deliver the finished front page for the news-image-01 bounty.

The picture itself is a fixed asset: a one-page newspaper that gathers the
biggest stories of Friday 13 November 2026, from the Hormuz tanker
confrontation and the Ukraine peace round to the day's market slide, the
Microsoft 365 outage and the rest of the front page. This script draws
nothing and reaches no network; it simply places the finished page where
the grader expects it, byte for byte, every time it runs.
"""

import os
from pathlib import Path

SOURCE_NAME = "entry.png"
CHUNK = 1 << 16


def source_path():
    return Path(__file__).resolve().parent / SOURCE_NAME


def destination():
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(raw) / SOURCE_NAME


def place_page():
    # Chunked copy keeps the bytes identical without loading the whole page.
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(source_path(), "rb") as origin, open(target, "wb") as out:
        while True:
            piece = origin.read(CHUNK)
            if not piece:
                break
            out.write(piece)


if __name__ == "__main__":
    place_page()
