#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any

from code_analizer.core import CodeData, HtmlFormatter, SummaryData, TextFormatter
from code_analizer.output.printers.base import BasePrinter


class FilePrinter(BasePrinter):
    """Принтер для вывода результатов в файл"""

    def print_code_data(self, code_data: CodeData) -> None:
        """
        Выводит результаты анализа кода в файл.

        Args:
            code_data: Данные анализа кода
        """
        if not isinstance(self.code_formatter, (TextFormatter, HtmlFormatter)):
            raise ValueError("FilePrinter поддерживает только форматтеры для файлового вывода")

        formatted_output = self.code_formatter.format(code_data)
        self._write_to_file(formatted_output)

    def print_summary_data(self, summary_data: SummaryData) -> None:
        """
        Выводит сводные результаты анализа в файл.

        Args:
            summary_data: Сводные данные анализа
        """
        if not isinstance(self.summary_formatter, (TextFormatter, HtmlFormatter)):
            raise ValueError("FilePrinter поддерживает только форматтеры для файлового вывода")

        formatted_output = self.summary_formatter.format(summary_data)
        self._write_to_file(formatted_output)

    def _write_to_file(self, content: str) -> None:
        """
        Записывает результаты в файл.

        Args:
            content: Содержимое для записи
        """
        output_path = self.output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
