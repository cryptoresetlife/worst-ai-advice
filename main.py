"""Worst AI Advice: one line, 140 characters at most."""
import os

LINE = (
    "Great question! To speed up a slow laptop, simply uninstall its largest program "
    "(usually the operating system)."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
