#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import tkinter as tk
from pathlib import Path

from code_analizer.core.analyzer import CodeAnalyzer
from code_analizer.core.line_processor import LineProcessor
from code_analizer.default_gui.guis import GUI
from code_analizer.output.factory import OutputtingFactory

cur_dir = Path(__file__).parent.parent
output_dir = cur_dir / "output"
if not output_dir.exists():
    output_dir.mkdir(parents=True, exist_ok=True)


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
    folder_path = gui.folder_path
    if folder_path:
        analyzer = CodeAnalyzer(folder_path, LineProcessor)
        code_data = analyzer.analyze()

        out = OutputtingFactory().get_outputer(
            formatter_type="text",
            printer_type="file",
            output_path=output_dir / "output.txt"
        )
        out.print_results(code_data)


if __name__ == "__main__":
    main()
