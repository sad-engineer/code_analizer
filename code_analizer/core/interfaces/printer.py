#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from pathlib import Path
from typing import Any, Optional, Protocol, Union, runtime_checkable

from code_analizer.core.data_classes import CodeData, SummaryData
from code_analizer.core.interfaces.formatter import IFormatter


@runtime_checkable
class IPrinter(Protocol):
    """Интерфейс для принтеров вывода"""

    def __init__(
        self, code_formatter: IFormatter, summary_formatter: IFormatter, output_path: Optional[Union[str, Path]] = None
    ) -> None:
        """
        Инициализация принтера.

        Args:
            formatter: Форматтер вывода
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
        ...

    def print_summary_data(self, summary_data: SummaryData) -> None:
        """
        Выводит сводные результаты анализа.

        Args:
            summary_data: Сводные данные анализа
        """
        ...
