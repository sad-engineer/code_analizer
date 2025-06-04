#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any

from code_analizer.core.interfaces.i_formatter import IFormatter


class BaseFormatter(IFormatter):
    """Базовый класс для всех форматтеров вывода"""

    def format_results(self, code_data: Any) -> str:
        """
        Форматирует результаты анализа кода.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: Отформатированный текст результатов
        """
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")
