#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Dict

from code_analizer.core.data_classes import CodeData, SummaryData
from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.settings.manager import get_setting


class JsonFormatter(BaseFormatter):
    """Форматтер вывода в JSON файл"""

    def format(self, code_data: CodeData) -> Dict[str, str]:
        """
        Форматирует результаты анализа в JSON.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: JSON-строка с результатами анализа
        """
        results = {
            "project_name": code_data.filename,
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


class JsonSummaryFormatter(BaseFormatter):
    """Форматтер вывода сводных данных в JSON файл"""

    def format(self, summary_data: SummaryData) -> Dict[str, str]:
        """
        Форматирует сводные результаты анализа в JSON.

        Args:
            summary_data: Сводные данные анализа кода

        Returns:
            Dict[str, str]: Словарь с результатами анализа в формате JSON
        """
        results = {
            "summary": {
                "total_files": summary_data.total_files,
                "statistics": {
                    "total_lines_of_code": summary_data.total_lines_of_code,
                    "total_comments": summary_data.total_comments,
                    "total_empty_lines": summary_data.total_empty_lines,
                    "total_classes": summary_data.total_classes,
                    "total_functions": summary_data.total_functions,
                    "total_constants": summary_data.total_constants,
                },
            }
        }

        if get_setting("details") == "full":
            results["summary"]["details"] = {
                "all_classes": sorted(list(summary_data.all_classes)),
                "all_functions": sorted(list(summary_data.all_functions)),
                "all_constants": sorted(list(summary_data.all_constants)),
            }

        return results
