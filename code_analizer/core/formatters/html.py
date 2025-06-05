#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from code_analizer.core.data_classes import CodeData, SummaryData
from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.settings.manager import get_setting


class HtmlFormatter(BaseFormatter):
    """Форматтер вывода в HTML файл"""

    def format(self, code_data: CodeData) -> str:
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
            <title>Анализ кода: {code_data.filename}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1, h2 {{ color: #333; }}
                .statistics {{ background: #f5f5f5; padding: 15px; border-radius: 5px; }}
                .details {{ margin-top: 20px; }}
                .item {{ margin: 5px 0; }}
            </style>
        </head>
        <body>
            <h1>Анализ кода: {code_data.filename}</h1>
            
            <div class="statistics">
                <h2>Статистика</h2>
                <p>Строк кода: {code_data.lines_of_code}</p>
                <p>Комментариев: {code_data.comments}</p>
                <p>Пустых строк: {code_data.empty_lines}</p>
                <p>Классов: {len(code_data.entities.classes)}</p>
                <p>Функций: {len(code_data.entities.functions)}</p>
                <p>Констант: {len(code_data.entities.constants)}</p>
            </div>
        """

        if get_setting("details") == "full":
            html += """
            <div class="details">
                <h2>Детали</h2>
                
                <h3>Классы</h3>
                <div class="item">
            """
            for cls in code_data.entities.classes:
                html += f"<p>{cls}</p>"

            html += """
                </div>
                <h3>Функции</h3>
                <div class="item">
            """
            for func in code_data.entities.functions:
                html += f"<p>{func}</p>"

            html += """
                </div>
                <h3>Константы</h3>
                <div class="item">
            """
            for const in code_data.entities.constants:
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


class HtmlSummaryFormatter(BaseFormatter):
    """Форматтер вывода сводных данных в HTML файл"""

    def format(self, summary_data: SummaryData) -> str:
        """
        Форматирует сводные результаты анализа в HTML.

        Args:
            summary_data: Сводные данные анализа кода

        Returns:
            str: HTML-разметка со сводными результатами анализа
        """
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Сводный анализ кода</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1, h2 {{ color: #333; }}
                .statistics {{ background: #f5f5f5; padding: 15px; border-radius: 5px; }}
                .details {{ margin-top: 20px; }}
                .item {{ margin: 5px 0; }}
                .summary-grid {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 20px;
                    margin-top: 20px;
                }}
                .summary-card {{
                    background: #fff;
                    padding: 15px;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .summary-card h3 {{
                    margin-top: 0;
                    color: #2c3e50;
                }}
                .summary-card p {{
                    margin: 5px 0;
                    color: #34495e;
                }}
            </style>
        </head>
        <body>
            <h1>Сводный анализ кода</h1>
            
            <div class="statistics">
                <h2>Общая статистика</h2>
                <div class="summary-grid">
                    <div class="summary-card">
                        <h3>Файлы</h3>
                        <p>Всего файлов: {summary_data.total_files}</p>
                    </div>
                    <div class="summary-card">
                        <h3>Строки кода</h3>
                        <p>Всего строк: {summary_data.total_lines_of_code}</p>
                        <p>Комментарии: {summary_data.total_comments}</p>
                        <p>Пустые строки: {summary_data.total_empty_lines}</p>
                    </div>
                    <div class="summary-card">
                        <h3>Сущности</h3>
                        <p>Классов: {summary_data.total_classes}</p>
                        <p>Функций: {summary_data.total_functions}</p>
                        <p>Констант: {summary_data.total_constants}</p>
                    </div>
                </div>
            </div>
        """

        if get_setting("details") == "full":
            html += """
            <div class="details">
                <h2>Детали</h2>
                
                <h3>Все классы</h3>
                <div class="item">
            """
            for cls in sorted(summary_data.all_classes):
                html += f"<p>{cls}</p>"

            html += """
                </div>
                <h3>Все функции</h3>
                <div class="item">
            """
            for func in sorted(summary_data.all_functions):
                html += f"<p>{func}</p>"

            html += """
                </div>
                <h3>Все константы</h3>
                <div class="item">
            """
            for const in sorted(summary_data.all_constants):
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
