#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any

from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.settings.manager import get_setting


class HtmlFormatter(BaseFormatter):
    """Форматтер вывода в HTML файл"""

    def format_results(self, code_data: Any) -> str:
        """
        Форматирует результаты анализа в HTML.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: HTML-разметка с результатами анализа
        """
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Анализ кода: {code_data.project_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1, h2 {{ color: #333; }}
                .statistics {{ background: #f5f5f5; padding: 15px; border-radius: 5px; }}
                .details {{ margin-top: 20px; }}
                .item {{ margin: 5px 0; }}
            </style>
        </head>
        <body>
            <h1>Анализ кода: {code_data.project_name}</h1>
            
            <div class="statistics">
                <h2>Статистика</h2>
                <p>Строк кода: {code_data.lines_of_code}</p>
                <p>Комментариев: {code_data.comments}</p>
                <p>Пустых строк: {code_data.empty_lines}</p>
                <p>Классов: {len(code_data.classes)}</p>
                <p>Функций: {len(code_data.functions)}</p>
                <p>Констант: {len(code_data.constants)}</p>
            </div>
        """

        if get_setting("details") == "full":
            html += """
            <div class="details">
                <h2>Детали</h2>
                
                <h3>Классы</h3>
                <div class="item">
            """
            for cls in code_data.classes:
                html += f"<p>{cls}</p>"

            html += """
                </div>
                <h3>Функции</h3>
                <div class="item">
            """
            for func in code_data.functions:
                html += f"<p>{func}</p>"

            html += """
                </div>
                <h3>Константы</h3>
                <div class="item">
            """
            for const in code_data.constants:
                html += f"<p>{const}</p>"

            html += """
                </div>
            </div>
            """

        html += """
        </body>
        </html>
        """

        return html
