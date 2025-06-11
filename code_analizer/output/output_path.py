#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from pathlib import Path

cur_dir = Path(__file__).parent.parent.parent
output_dir = cur_dir / "output"
if not output_dir.exists():
    output_dir.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH = output_dir / "output.txt"
