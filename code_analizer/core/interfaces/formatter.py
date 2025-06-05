#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class IFormatter(Protocol):
    """Протокол для форматтеров вывода"""

    def format(self, code_data: Any) -> str:
        """
        Форматирует результаты анализа кода.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: Отформатированный текст результатов
        """
        ...
