#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import List

from code_analizer.core.code_text_analyzer import CodeTextAnalyzer
from code_analizer.core.data_classes import CodeData, SummaryData
from code_analizer.core.interfaces import IUploadFile


class FileBatchAnalyzer:
    """
    Класс для пакетного анализа списка файлов с помощью CodeTextAnalyzer.
    Каждый файл подается в виде кортежа (имя_файла, текст_файла).
    """

    def __init__(self, line_processor):
        self.analyzer = CodeTextAnalyzer(line_processor)

    async def analyze_file(self, file: IUploadFile) -> CodeData:
        """
        Анализирует файл.

        file должен иметь:
          - атрибут .filename (имя файла)
          - метод .read() -> bytes или str (содержимое файла)
        """
        content = await file.read()
        code = content.decode()
        return self.analyzer.analyze(code, file.filename)

    async def analyze_files(self, files: List[IUploadFile]) -> List[CodeData]:
        """Анализирует список файлов."""
        self.files_data = [await self.analyze_file(file) for file in files]
        return self.files_data

    def get_summary(self) -> SummaryData:
        """
        Получает сводные данные по всем проанализированным файлам.

        Args:
            files_data: Список результатов анализа файлов

        Returns:
            SummaryData: Сводные данные по всем файлам
        """
        summary_data = SummaryData(
            total_files=0,
            total_lines_of_code=0,
            total_comments=0,
            total_empty_lines=0,
            total_classes=0,
            total_functions=0,
            total_constants=0,
            all_classes=set(),
            all_functions=set(),
            all_constants=set(),
        )

        for file_data in self.files_data:
            summary_data.total_files += 1
            summary_data.total_lines_of_code += file_data.lines_of_code
            summary_data.total_comments += file_data.comments
            summary_data.total_empty_lines += file_data.empty_lines
            summary_data.total_classes += len(file_data.entities.classes)
            summary_data.total_functions += len(file_data.entities.functions)
            summary_data.total_constants += len(file_data.entities.constants)

            summary_data.all_classes.update(file_data.entities.classes)
            summary_data.all_functions.update(file_data.entities.functions)
            summary_data.all_constants.update(file_data.entities.constants)

        return summary_data
