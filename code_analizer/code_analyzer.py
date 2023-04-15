#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
from pathlib import Path


class CodeAnalyzer:
    """
    Класс, выполняющий анализ кода.

    Атрибуты:
    -----------
    folder_path : str
        Путь к папке, в которой находятся файлы для анализа.
    file_list : list
        Список всех файлов с расширением .py в папке folder_path.
    lines_of_code : int
        Количество строк кода в анализируемых файлах.
    comments : int
        Количество комментариев в анализируемых файлах.
    classes : int
        Количество классов в анализируемых файлах.
    functions : int
        Количество функций в анализируемых файлах.
    constants : int
        Количество констант в анализируемых файлах.

    Методы:
    --------
    analyze()
        Анализирует все файлы с расширением .py в папке folder_path.
        Для каждого файла определяет количество строк кода, комментариев, классов, функций и констант.
    print_results(output_handler)
        Выводит результаты анализа в заданный объект output_handler.

    Пример использования:
    ---------------------
    analyzer = CodeAnalyzer('/path/to/folder')
    analyzer.analyze()
    console_output_handler = ConsoleOutputHandler()
    file_output_handler = FileOutputHandler('output.txt')
    analyzer.print_results(console_output_handler)
    analyzer.print_results(file_output_handler)
    """

    def __init__(self, folder_path, line_processor):
        """
        Parameters:
        -----------
        folder_path : str
            Путь к папке, в которой находятся файлы для анализа.
        """
        self.folder_path: str = folder_path
        self.project_name: str = ""
        self.file_list: tuple = []
        self.lines_of_code: int = 0
        self.comments: int = 0
        self.empty_lines: int = 0
        self.classes: set = set()
        self.functions: set = set()
        self.constants: set = set()
        self.line_processor = line_processor

    def analyze(self):
        """Анализирует все файлы с расширением .py в папке folder_path.
        Для каждого файла определяет количество строк кода, комментариев, классов, функций и констант."""
        self.project_name = self.folder_path.split("/")[-1]
        self.file_list = list(Path(self.folder_path).rglob("*.py"))
        for file_path in self.file_list:
            if "__pycache__" in str(file_path):
                continue
            with open(file_path, "r", encoding="utf8") as f:
                lines = f.readlines()
                for line in lines:
                    line_processor = self.line_processor(line)
                    line_type = line_processor.process_line()
                    if line_type == "code":
                        self.lines_of_code += 1
                    elif line_type == "comment":
                        self.comments += 1
                    elif line_type == "empty":
                        self.empty_lines += 1
                    elif line_type == "class":
                        class_name = line.strip().split()[1].split("(")[0].replace(":", "")
                        self.classes.add(f"{class_name} in {file_path}")
                    elif line_type == "function":
                        function_name = line.strip().split()[1].split("(")[0]
                        self.functions.add(f"{function_name} in {file_path}")
                    elif line_type == "constant":
                        constant_name = line.strip().strip(' .,"').split()[0]
                        self.constants.add(f"{constant_name}")
