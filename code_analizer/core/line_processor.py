#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
class LineProcessor:
    """
    Класс определяет тип строки.

    Parameters:
    line (str): Строка кода для обработки.
    """
    @staticmethod
    def process_line(line) -> str:
        """
        Метод, который определяет тип строки.

        Returns:
        str: Тип строки - пустая строка, комментарий, класс, функция, константа или код.
        """
        line = line.strip()
        if not line.strip():
            return "empty"
        if line.startswith("#"):
            return "comment"
        if line.startswith("class "):
            return "class"
        if line.startswith("def "):
            return "function"
        if line.split("=")[0].isupper():
            return "constant"
        return "code"
