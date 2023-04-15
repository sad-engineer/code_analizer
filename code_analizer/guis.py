#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog

from .code_analyzer import CodeAnalyzer
from .line_processor import LineProcessor
from .output_handlers import FileOutputHandler, ConsoleOutputHandler


class GUI:
    def __init__(self, master):
        """
        Инициализация GUI с переданным главным окном.

        :param master: экземпляр главного окна
        """
        self.master = master
        self.folder_path = ""
        self.select_folder_button = tk.Button(
            self.master,
            text="Select Project Folder",
            command=self.select_folder,
        )
        self.select_folder_button.pack()

    def select_folder(self):
        """
        Обработчик нажатия на кнопку "Select Project Folder". Открывает диалоговое окно выбора папки, запускает
        анализатор кода и выводит результаты анализа в консоль и файл.
        """
        self.folder_path = filedialog.askdirectory()
        self.master.destroy()
        # self.folder_path = filedialog.askdirectory()
        # if self.folder_path:
        #     analyzer = CodeAnalyzer(self.folder_path, LineProcessor)
        #     analyzer.analyze()
        #     console_output_handler = ConsoleOutputHandler()
        #     file_output_handler = FileOutputHandler("output.txt")
        #     analyzer.print_results(console_output_handler)
        #     analyzer.print_results(file_output_handler)
