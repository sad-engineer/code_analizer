#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import List
from code_analizer.core.code_text_analyzer import CodeTextAnalyzer
from code_analizer.core.data_classes import CodeData
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
        """ Анализирует список файлов."""
        return [await self.analyze_file(file) for file in files]
