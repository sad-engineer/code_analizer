#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
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
    formatted_data = "\n".join(data_list)
    return {
        "summary": f"{data_len}",
        "details": f"{formatted_data}",
        "full": f"{data_len}\n{formatted_data}"
    }.get(setting)


class FileOutputHandler:
    """
    Класс, который записывает результаты анализа в файл

    :param output_file_path: Путь к файлу, в который будут записываться результаты анализа
    """

    def __init__(self, output_file_path) -> None:
        self.output_file_path = output_file_path
        open(self.output_file_path, 'w').close()

    def print(self, output_string) -> None:
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
        title = f"Анализируемый пакет: {code_data.project_name}"
        output(title)

        prefix = "Количество классов пакета: "
        len_classes_str = format_set(code_data.classes, setting="summary").replace("\n", ", ")
        output("".join([prefix, len_classes_str, "."]))

        prefix = "Количество функций пакета: "
        len_classes_str = format_set(code_data.functions, setting="summary").replace("\n", ", ")
        output("".join([prefix, len_classes_str, "."]))

        prefix = "Количество констант пакета: "
        len_classes_str = format_set(code_data.constants, setting="summary").replace("\n", ", ")
        output("".join([prefix, len_classes_str, "."]))

        prefix = "Количество строк кода пакета: "
        len_classes_str = str(code_data.lines_of_code)
        output("".join([prefix, len_classes_str, "."]))

        prefix = "Количество строк комментариев: "
        len_classes_str = str(code_data.comments)
        output("".join([prefix, len_classes_str, "."]))
