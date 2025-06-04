#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from pathlib import Path
from typing import Any, Optional, Union

from code_analizer.core.interfaces import IFormatter
from code_analizer.core.interfaces.i_printer import IPrinter


class BasePrinter(IPrinter):
    """Базовый класс для всех принтеров"""

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
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")
