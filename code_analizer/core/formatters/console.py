#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any

from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.settings.manager import get_setting


class ConsoleFormatter(BaseFormatter):
    """Форматтер вывода в консоль"""

    def format_results(self, code_data: Any) -> str:
        """
        Форматирует результаты анализа для вывода в консоль.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: Отформатированный текст результатов
        """
        output = [self._format_title(code_data), self._format_statistics(code_data), self._format_details(code_data)]
        return "\n".join(output)

    @staticmethod
    def _format_title(code_data: Any) -> str:
        """Форматирование заголовка"""
        return f"\nАнализируемый пакет: {code_data.project_name}\n" + "-" * 50

    @staticmethod
    def _format_statistics(code_data: Any) -> str:
        """Форматирование статистики"""
        stats = [
            "\nСтатистика:",
            f"Строк кода: {code_data.lines_of_code}",
            f"Комментариев: {code_data.comments}",
            f"Пустых строк: {code_data.empty_lines}",
            f"Классов: {len(code_data.classes)}",
            f"Функций: {len(code_data.functions)}",
            f"Констант: {len(code_data.constants)}",
        ]
        return "\n".join(stats)

    @staticmethod
    def _format_details(code_data: Any) -> str:
        """Форматирование деталей"""
        if get_setting("details") != "full":
            return ""

        details = ["\nДетали:"]

        details.append("\nКлассы:")
        details.extend([f"  - {cls}" for cls in code_data.classes])

        details.append("\nФункции:")
        details.extend([f"  - {func}" for func in code_data.functions])

        details.append("\nКонстанты:")
        details.extend([f"  - {const}" for const in code_data.constants])

        return "\n".join(details)
