#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
class LineProcessor:
    def __init__(self, line):
        """
        Конструктор класса LineProcessor.

        Parameters:
        line (str): Строка кода для обработки.

        Returns:
        None.
        """
        self.line = line.strip()

    def process_line(self):
        """
        Метод, который определяет тип строки.

        Parameters:
        None.

        Returns:
        str: Тип строки - комментарий, класс, функция, константа или код.
        """
        if not self.line.strip():
            return "empty"
        if self.line.startswith("#"):
            return "comment"
        if self.line.startswith("class "):
            return "class"
        if self.line.startswith("def "):
            return "function"
        if self.line.split("=")[0].isupper():
            return "constant"
        # if "=" in self.line:
        #     if "==" not in self.line:
        #         data = self.line.split("=")
        #         if len(data) == 2:
        #             left, right = self.line.split("=")
        #             if left.isupper():
        #                 return "constant"
        return "code"
