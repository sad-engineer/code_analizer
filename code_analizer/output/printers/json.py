#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
import json
from typing import Any

from code_analizer.core import CodeData, JsonFormatter, SummaryData
from code_analizer.output.printers.base import BasePrinter


class JsonPrinter(BasePrinter):
    """Принтер для вывода результатов в JSON файл"""

    def print_code_data(self, code_data: CodeData) -> None:
        """
        Выводит результаты анализа кода в JSON файл.

        Args:
            code_data: Данные анализа кода
        """
        if not isinstance(self.code_formatter, JsonFormatter):
            raise ValueError("JsonPrinter поддерживает только JsonFormatter")

        formatted_output = self.code_formatter.format(code_data)
        self._write_to_file(formatted_output)

    def print_summary_data(self, summary_data: SummaryData) -> None:
        """
        Выводит сводные результаты анализа в JSON файл.

        Args:
            summary_data: Сводные данные анализа
        """
        if not isinstance(self.summary_formatter, JsonFormatter):
            raise ValueError("JsonPrinter поддерживает только JsonFormatter")

        formatted_output = self.summary_formatter.format(summary_data)
        self._write_to_file(formatted_output)

    def _write_to_file(self, content: dict) -> None:
        """
        Записывает JSON результаты в файл.

        Args:
            content: Словарь с данными для записи
        """
        if not hasattr(self.formatter, 'output_file_path'):
            return

        output_path = self.output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
