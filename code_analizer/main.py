#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
import asyncio
import tkinter as tk
from pathlib import Path

from code_analizer.core import FileBatchAnalyzer
from code_analizer.core import LineProcessor
from code_analizer.default_gui.guis import GUI
from code_analizer.output import OutputtingFactory, OUTPUT_PATH
from code_analizer.scr import default_analyze_project as analyze_project

analyzer = FileBatchAnalyzer(line_processor=LineProcessor)
outputer = OutputtingFactory().get_outputer(output_path=OUTPUT_PATH)


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

    folder_path = gui.folder_path
    if not folder_path:
        print("Директория не выбрана")
        return
    files_data, summary = asyncio.run(analyze_project(folder_path))
    outputer.print_results(files_data, summary)
    print("Анализ завершен!")


if __name__ == "__main__":
    main()
