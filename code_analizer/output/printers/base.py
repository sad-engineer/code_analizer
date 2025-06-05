#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from pathlib import Path
from typing import Any, Optional, Union

from code_analizer.core import CodeData, IFormatter, IPrinter, SummaryData


class BasePrinter(IPrinter):
    """Базовый класс для всех принтеров"""

    def __init__(
        self, code_formatter: IFormatter, summary_formatter: IFormatter, output_path: Optional[Union[str, Path]] = None
    ) -> None:
        """
        Инициализация принтера.

        Args:
            code_formatter: Форматтер вывода для анализа кода
            summary_formatter: Форматтер вывода для сводных данных
            output_path: Путь для вывода результатов
        """
        self.code_formatter = code_formatter
        self.summary_formatter = summary_formatter
        self.output_path = output_path

    def print_code_data(self, code_data: CodeData) -> None:
        """
        Выводит результаты анализа кода.

        Args:
            code_data: Данные анализа кода
        """
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")

    def print_summary_data(self, summary_data: SummaryData) -> None:
        """
        Выводит сводные результаты анализа.

        Args:
            summary_data: Сводные данные анализа
        """
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")
