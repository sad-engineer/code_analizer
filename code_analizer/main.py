#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import tkinter as tk
from code_analizer.guis import GUI
from code_analizer.code_analyzer import CodeAnalyzer
from code_analizer.line_processor import LineProcessor
from code_analizer.output_handlers import FileOutputHandler, ConsoleOutputHandler, OutputResultHandler


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
    folder_path = gui.folder_path
    if folder_path:
        analyzer = CodeAnalyzer(folder_path, LineProcessor)
        analyzer.analyze()

        OutputResultHandler().print_results(code_data=analyzer, output=ConsoleOutputHandler().print)
        #
        # console_output_handler = ConsoleOutputHandler().print
        # analyzer.print_results(output=console_output_handler)
        #
        # file_output_handler = FileOutputHandler("/".join([folder_path, "output.txt"])).print
        # analyzer.print_results(output=file_output_handler)


if __name__ == '__main__':
    main()
