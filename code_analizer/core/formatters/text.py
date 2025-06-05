#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from code_analizer.core.data_classes import CodeData, SummaryData
from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.settings.manager import get_setting


class TextFormatter(BaseFormatter):
    """Форматтер вывода в текстовый файл"""

    def format(self, code_data: CodeData) -> str:
        """
        Форматирует результаты анализа для записи в файл.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: Отформатированный текст результатов
        """
        output = [
            f"Анализируемый пакет: {code_data.filename}",
            "-" * 50,
            "",
            "Статистика:",
            f"Строк кода: {code_data.lines_of_code}",
            f"Комментариев: {code_data.comments}",
            f"Пустых строк: {code_data.empty_lines}",
            f"Классов: {len(code_data.entities.classes)}",
            f"Функций: {len(code_data.entities.functions)}",
            f"Констант: {len(code_data.entities.constants)}",
            "",
        ]

        if get_setting("details") == "full":
            output.append("Детали:")
            output.append("\nКлассы:")
            output.extend([f"  - {cls}" for cls in code_data.entities.classes])
            output.append("\nФункции:")
            output.extend([f"  - {func}" for func in code_data.entities.functions])
            output.append("\nКонстанты:")
            output.extend([f"  - {const}" for const in code_data.entities.constants])

        return "\n".join(output)


class TextSummaryFormatter(BaseFormatter):
    """Форматтер вывода сводных данных в текстовый файл"""

    def format(self, summary_data: SummaryData) -> str:
        """
        Форматирует сводные результаты анализа для записи в файл.

        Args:
            summary_data: Сводные данные анализа кода

        Returns:
            str: Отформатированный текст сводных результатов
        """
        output = [
            "Сводный анализ кода",
            "=" * 50,
            "",
            "Общая статистика:",
            f"Всего файлов: {summary_data.total_files}",
            f"Всего строк кода: {summary_data.total_lines_of_code}",
            f"Всего комментариев: {summary_data.total_comments}",
            f"Всего пустых строк: {summary_data.total_empty_lines}",
            f"Всего классов: {summary_data.total_classes}",
            f"Всего функций: {summary_data.total_functions}",
            f"Всего констант: {summary_data.total_constants}",
            "",
        ]

        if get_setting("details") == "full":
            output.append("Детали:")
            output.append("\nВсе классы:")
            output.extend([f"  - {cls}" for cls in sorted(summary_data.all_classes)])
            output.append("\nВсе функции:")
            output.extend([f"  - {func}" for func in sorted(summary_data.all_functions)])
            output.append("\nВсе константы:")
            output.extend([f"  - {const}" for const in sorted(summary_data.all_constants)])

        return "\n".join(output)
