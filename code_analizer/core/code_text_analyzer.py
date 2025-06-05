#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
from code_analizer.core.data_classes import CodeData


class CodeTextAnalyzer:
    """
    Класс, выполняющий анализ кода по тексту файла.

    Атрибуты:
    -----------
    line_processor : класс
        Класс для обработки строк.

    Методы:
    --------
    analyze(text: str, filename: str = "file.py")
        Анализирует переданный текст файла.
    """

    def __init__(self, line_processor):
        self.line_processor = line_processor()

    def analyze(self, text: str, filename: str = "file.py") -> CodeData:
        """
        Анализирует переданный текст файла.

        Args:
            text: str - текст файла
            filename: str - имя файла (для отчета)
        Returns:
            CodeData
        """
        code_data = CodeData(
            filename=filename,
            lines_of_code=0,
            comments=0,
            empty_lines=0,
            classes=set(),
            functions=set(),
            constants=set(),
            file_content=text,
        )
        lines = text.splitlines()
        for line in lines:
            line_type = self.line_processor.process_line(line)
            if line_type == "code":
                code_data.lines_of_code += 1
            elif line_type == "comment":
                code_data.comments += 1
            elif line_type == "empty":
                code_data.empty_lines += 1
            elif line_type == "class":
                class_name = line.strip().split()[1].split("(")[0].replace(":", "")
                code_data.entities.classes.add(f"{class_name} in {filename}")
            elif line_type == "function":
                function_name = line.strip().split()[1].split("(")[0]
                code_data.entities.functions.add(f"{function_name} in {filename}")
            elif line_type == "constant":
                constant_name = line.strip().strip(' .,"').split()[0]
                code_data.entities.constants.add(f"{constant_name}")
        return code_data
