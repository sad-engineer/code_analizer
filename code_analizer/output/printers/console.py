#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any

from code_analizer.core import CodeData, ConsoleFormatter, ConsoleSummaryFormatter, SummaryData
from code_analizer.output.printers.base import BasePrinter


class ConsolePrinter(BasePrinter):
    """Принтер для вывода результатов в консоль"""

    def print_code_data(self, code_data: CodeData) -> None:
        """
        Выводит результаты анализа кода в консоль.

        Args:
            code_data: Данные анализа кода
        """
        if not isinstance(self.code_formatter, ConsoleFormatter):
            raise ValueError("print_code_data поддерживает только ConsoleFormatter")

        formatted_output = self.code_formatter.format(code_data)
        print(formatted_output)

    def print_summary_data(self, summary_data: SummaryData) -> None:
        """
        Выводит сводные результаты анализа в консоль.

        Args:
            summary_data: Сводные данные анализа
        """
        if not isinstance(self.summary_formatter, ConsoleSummaryFormatter):
            raise ValueError("print_summary_data поддерживает только ConsoleSummaryFormatter")

        formatted_output = self.summary_formatter.format(summary_data)
        print(formatted_output)
