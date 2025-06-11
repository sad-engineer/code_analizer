#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from pathlib import Path
from typing import List, Optional, Type, Union

from code_analizer.core import CODE_FORMATTERS, SUMMARY_FORMATTERS, CodeData, IFormatter, IPrinter, SummaryData
from code_analizer.output.printers import PRINTERS


class Outputting:
    def __init__(
        self,
        code_formatter_class: Type[IFormatter],
        summary_formatter_class: Type[IFormatter],
        printer_class: Type[IPrinter],
        output_path: Optional[Union[str, Path]] = None,
    ):
        self.code_formatter_class = code_formatter_class
        self.summary_formatter_class = summary_formatter_class
        self.printer_class = printer_class
        self.output_path = output_path

    def print_results(self, code_data: Union[CodeData, List[CodeData]], summary_data: SummaryData) -> None:
        """Выводит результаты анализа кода в указанный тип вывода"""
        code_formatter = self.code_formatter_class()
        summary_formatter = self.summary_formatter_class()
        printer = self.printer_class(
            code_formatter=code_formatter, summary_formatter=summary_formatter, output_path=self.output_path
        )
        if isinstance(code_data, list):
            [printer.print_code_data(data) for data in code_data]
        else:
            printer.print_code_data(code_data)
        printer.print_summary_data(summary_data)


class OutputtingFactory:
    """Фабрика для создания форматтеров вывода"""

    _code_formatters = CODE_FORMATTERS
    _summary_formatters = SUMMARY_FORMATTERS
    _printers = PRINTERS

    def get_outputer(
        self, formatter_type: str = "text", printer_type: str = "file", output_path: Optional[Union[str, Path]] = None
    ) -> Outputting:
        """
        Создает объект для вывода результатов анализа кода.

        Args:
            formatter_type: str - Тип форматтера
            printer_type: str - Тип принтера
            output_path: Optional[Union[str, Path]] = None - Путь для вывода результатов

        Raises:
            ValueError: Если указан неизвестный тип форматтера
            ValueError: Если не указан путь для форматтеров, требующих файл
        """
        formatter_type = formatter_type.lower()
        printer_type = printer_type.lower()

        if all(
            [
                self._check_formatter(formatter_type),
                self._check_printer(printer_type),
                self._check_output_path(output_path) if printer_type != "console" else True,
            ]
        ):
            if printer_type != "console":
                self._check_output_path(output_path),
            code_formatter_class = self._code_formatters[formatter_type]
            summary_formatter_class = self._summary_formatters[formatter_type]
            printer_class = self._printers[printer_type]

            return Outputting(code_formatter_class, summary_formatter_class, printer_class, output_path)
        else:
            raise ValueError("Некорректные параметры для создания объекта вывода")

    def get_available_code_formatters(self) -> list[str]:
        """
        Возвращает список доступных типов форматтеров для анализа кода.

        Returns:
            list[str]: Список доступных типов форматтеров
        """
        return list(self._code_formatters.keys())

    def get_available_summary_formatters(self) -> list[str]:
        """
        Возвращает список доступных типов форматтеров для сводных данных.

        Returns:
            list[str]: Список доступных типов форматтеров
        """
        return list(self._summary_formatters.keys())

    def get_available_printers(self) -> list[str]:
        """
        Возвращает список доступных типов принтеров.

        Returns:
            list[str]: Список доступных типов принтеров
        """
        return list(self._printers.keys())

    def _check_formatter(self, formatter: str) -> bool:
        """Проверяет, является ли тип форматтера доступным"""
        if not isinstance(formatter, str):
            raise ValueError("Тип форматтера должен быть строкой")
        if formatter not in self._code_formatters and formatter not in self._summary_formatters:
            raise ValueError(
                f"Неизвестный тип форматтера: {formatter}. Доступные типы: {', '.join(self.get_available_code_formatters() + self.get_available_summary_formatters())}"
            )
        return True

    def _check_printer(self, printer: str) -> bool:
        """Проверяет, является ли тип принтера доступным"""
        if not isinstance(printer, str):
            raise ValueError("Тип принтера должен быть строкой")
        if printer not in self._printers:
            raise ValueError(
                f"Неизвестный тип принтера: {printer}. Доступные типы: {', '.join(self.get_available_printers())}"
            )
        return True

    def _check_output_path(self, output_path: Optional[Union[str, Path]] = None) -> bool:
        """Проверяет, является ли путь для вывода результатов доступным"""
        if output_path is None:
            raise ValueError("Путь для вывода результатов не указан")
        if not isinstance(output_path, (str, Path)):
            raise ValueError(
                f"Путь для вывода результатов должен быть строкой или объектом Path. Получено: {output_path} ({type(output_path)})"
            )
        return True


if __name__ == "__main__":
    code_data = "print('Hello, World!')"
    outputer = OutputtingFactory().get_outputer(formatter_type="text", printer_type="file", output_path="output.txt")
    outputer.print_results(code_data)
