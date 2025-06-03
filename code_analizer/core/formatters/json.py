#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any, Dict

from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.settings.manager import get_setting


class JsonFormatter(BaseFormatter):
    """Форматтер вывода в JSON файл"""

    def format_results(self, code_data: Any) -> Dict[str, str]:
        """
        Форматирует результаты анализа в JSON.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: JSON-строка с результатами анализа
        """
        results = {
            "project_name": code_data.project_name,
            "statistics": {
                "lines_of_code": code_data.lines_of_code,
                "comments": code_data.comments,
                "empty_lines": code_data.empty_lines,
                "classes": len(code_data.entities.classes),
                "functions": len(code_data.entities.functions),
                "constants": len(code_data.entities.constants),
            },
        }

        if get_setting("details") == "full":
            results["details"] = {
                "classes": list(code_data.entities.classes),
                "functions": list(code_data.entities.functions),
                "constants": list(code_data.entities.constants),
            }

        return results
