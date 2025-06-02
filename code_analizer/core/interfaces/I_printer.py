#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class IPrinter(Protocol):
    """Интерфейс для принтеров вывода"""

    def print_results(self, code_data: Any) -> None:
        """
        Выводит результаты анализа кода.

        Args:
            code_data: Данные анализа кода
        """
        ...
