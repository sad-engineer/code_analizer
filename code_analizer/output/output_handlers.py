#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
from code_analizer.settings.manager import get_setting


def format_set(data_set, setting="summary") -> str:
    """
    Функция для форматирования множества.

    Parameters:
    data_set (set): Множество для форматирования.
    setting ("summary", "details", "full"): Переключатель, указывающий, нужно ли вернуть только суммарные данные
    ('summary'), детализированные данные ("details") или все данные ("full").

    Returns:
    str: Отформатированные данные множества.
    """

    data_len = str(len(data_set))
    data_list = list(data_set)
    formatted_data = "".join(["    " + item + "\n" for item in data_list])
    return {
        "summary": f"{data_len}",
        "details": f"{formatted_data}",
        "full": f"{data_len}\n{formatted_data}",
    }.get(setting)


class FileOutputHandler:
    """
    Класс, который записывает результаты анализа в файл

    :param output_file_path: Путь к файлу, в который будут записываться результаты анализа
    """

    def __init__(self, output_file_path) -> None:
        self.output_file_path = output_file_path
        open(self.output_file_path, "w").close()

    def print_results(self, output_string) -> None:
        """
        Метод, который записывает переданную строку в файл

        :param output_string: Строка для записи
        """
        with open(self.output_file_path, "a", encoding="utf8") as f:
            f.write(output_string + "\n")


class OutputResultHandler:
    """
    Класс, который выводит результат
    """

    @staticmethod
    def print_results(code_data, output=print) -> None:
        """
        Метод, который выводит результаты анализа кода проекта (code_data)

        :param code_data: анализа кода проекта
        :param output: метод OutputHandler'а (который реализует процедуру вывода строки куда-либо.
        Например FileOutputHandler.print(line))
        """

        def print_set(token, set_, setting="minimum"):
            """Внутренняя функция, выводит множество на печать"""
            prefix = f"Количество {token} пакета: "
            len_classes_str = format_set(set_, setting="summary").replace("\n", ", ")
            output("".join([prefix, len_classes_str, "."]))
            if setting == "full":
                output("Пакет содержит: ")
                list_classes = format_set(set_, setting="details")[:-2]
                output(list_classes)

        details = get_setting("details")

        title = f"Анализируемый пакет: {code_data.project_name}"
        output(title)

        print_set(token="классов", set_=code_data.classes, setting=details)
        output("")

        print_set(token="функций", set_=code_data.functions, setting=details)
        output("")

        print_set(token="констант", set_=code_data.constants, setting=details)
        output("")

        prefix = "Количество строк кода пакета: "
        len_lines_of_code_str = str(code_data.lines_of_code)
        output("".join([prefix, len_lines_of_code_str, "."]))
        output("")

        prefix = "Количество строк комментариев: "
        len_comments_str = str(code_data.comments)
        output("".join([prefix, len_comments_str, "."]))
        output("")

        prefix = "Количество пустых строк: "
        len_empty_lines_str = str(code_data.empty_lines)
        output("".join([prefix, len_empty_lines_str, "."]))
        output("")
