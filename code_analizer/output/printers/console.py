#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any

from code_analizer.core.formatters import ConsoleFormatter
from code_analizer.output.printers.base import BasePrinter


class ConsolePrinter(BasePrinter):
    """Принтер для вывода результатов в консоль"""

    def print_results(self, code_data: Any) -> None:
        """
        Выводит результаты анализа кода в консоль.

        Args:
            code_data: Данные анализа кода
        """
        if not isinstance(self.formatter, ConsoleFormatter):
            raise ValueError("ConsolePrinter поддерживает только ConsoleFormatter")

        formatted_output = self.formatter.format_results(code_data)
        print(formatted_output)
