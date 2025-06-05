#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from code_analizer.core.data_classes import CodeData
from code_analizer.core.interfaces.formatter import IFormatter


class BaseFormatter(IFormatter):
    """Базовый класс для всех форматтеров вывода"""

    def format_results(self, code_data: CodeData) -> str:
        """
        Форматирует результаты анализа кода.

        Args:
            code_data: Данные анализа кода

        Returns:
            str: Отформатированный текст результатов
        """
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")
