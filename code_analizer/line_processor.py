#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
class LineProcessor:
    """
    Класс определяет тип строки.

    Parameters:
    line (str): Строка кода для обработки.
    """

    def __init__(self, line) -> None:
        self.line = line.strip()

    def process_line(self) -> str:
        """
        Метод, который определяет тип строки.

        Returns:
        str: Тип строки - пустая строка, комментарий, класс, функция, константа или код.
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
        return "code"
