#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import tkinter as tk

from code_analizer.core.code_analyzer import CodeAnalyzer
from code_analizer.default_gui.guis import GUI
from code_analizer.core.line_processor import LineProcessor
from code_analizer.output.output_handlers import OutputResultHandler


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
    folder_path = gui.folder_path
    if folder_path:
        analyzer = CodeAnalyzer(folder_path, LineProcessor)
        analyzer.analyze()

        OutputResultHandler().print_results(code_data=analyzer)


if __name__ == "__main__":
    main()
