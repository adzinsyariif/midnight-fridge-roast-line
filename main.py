#!/usr/bin/env python3
import os

LINE = "You lock at midnight to stop my snacking — bold for a box whose whole job is keeping snacks cold until I'm weak enough to want them."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
