#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from pathlib import Path
from typing import Any, Optional, Protocol, Union, runtime_checkable

from code_analizer.core.interfaces.formatter import IFormatter


@runtime_checkable
class IPrinter(Protocol):
    """Интерфейс для принтеров вывода"""

    def __init__(self, formatter: IFormatter, output_path: Optional[Union[str, Path]] = None) -> None:
        """
        Инициализация принтера.

        Args:
            formatter: Форматтер вывода
            output_path: Путь для вывода результатов
        """
        self.formatter = formatter
        self.output_path = output_path

    def print_results(self, code_data: Any) -> None:
        """
        Выводит результаты анализа кода.

        Args:
            code_data: Данные анализа кода
        """
        ...
