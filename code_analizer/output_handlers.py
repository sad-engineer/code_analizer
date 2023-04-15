#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
def format_set(data_set, setting="summary"):
    """
    Функция для форматирования множества.

    Parameters:
    data_set (set): Множество для форматирования.
    summary (bool): Переключатель, указывающий, нужно ли вернуть только суммарные данные (True), детализированные данные (False) или все данные (None).

    Returns:
    str: Отформатированные данные множества.
    """
    data_len = str(len(data_set))
    data_list = list(data_set)
    formatted_data = "\n".join(data_list)

    return {
        "summary": f"{data_len}",
        "details": f"{formatted_data}",
        "full": f"{data_len}\n{formatted_data}"
    }.get(setting)


class ConsoleOutputHandler:
    """
    Класс, который выводит результаты анализа на консоль
    """

    @staticmethod
    def print(output_string):
        """
        Метод, который выводит переданную строку на консоль

        :param output_string: Строка для вывода
        """
        print(output_string)


class FileOutputHandler:
    """
    Класс, который записывает результаты анализа в файл
    """

    def __init__(self, output_file_path):
        """
        Конструктор класса

        :param output_file_path: Путь к файлу, в который будут записываться результаты анализа
        """
        self.output_file_path = output_file_path

    def print(self, output_string):
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
    def print_results(code_data, output=print):
        """
        Метод, который выводит результаты анализа кода проекта (code_data)

        :param code_data: анализа кода проекта
        """

        preffix = "Количество классов пакета: "
        len_classes_str = format_set(code_data.classes, setting="summary").replace("\n", ", ")
        output("".join([preffix, len_classes_str, "."]))

        preffix = "Количество функций пакета: "
        len_classes_str = format_set(code_data.functions, setting="summary").replace("\n", ", ")
        output("".join([preffix, len_classes_str, "."]))

        preffix = "Количество констант пакета: "
        len_classes_str = format_set(code_data.constants, setting="summary").replace("\n", ", ")
        output("".join([preffix, len_classes_str, "."]))

        preffix = "Количество строк кода: "
        len_classes_str = str(code_data.lines_of_code)
        output("".join([preffix, len_classes_str, "."]))

        preffix = "Количество строк комментариев: "
        len_classes_str = str(code_data.comments)
        output("".join([preffix, len_classes_str, "."]))
