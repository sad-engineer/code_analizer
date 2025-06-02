#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from pathlib import Path
from typing import Any, Union

from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.settings.manager import get_setting


class TextFormatter(BaseFormatter):
    """Форматтер вывода в текстовый файл"""

    def format_results(self, code_data: Any) -> str:
        """
        Форматирует результаты анализа для записи в файл.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: Отформатированный текст результатов
        """
        output = [
            f"Анализируемый пакет: {code_data.project_name}",
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
            output.extend([f"  - {cls}" for cls in code_data.classes])
            output.append("\nФункции:")
            output.extend([f"  - {func}" for func in code_data.functions])
            output.append("\nКонстанты:")
            output.extend([f"  - {const}" for const in code_data.constants])

        return "\n".join(output)
