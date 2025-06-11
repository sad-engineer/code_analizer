#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
from pathlib import Path

from code_analizer.core import CodeData, FileBatchAnalyzer, LineProcessor, SummaryData
from code_analizer.core.wrappers import FileWrapper

analyzer = FileBatchAnalyzer(line_processor=LineProcessor)


async def default_analyze_project(folder_path: Path) -> tuple[list[CodeData], SummaryData]:
    """Асинхронная функция для анализа проекта"""
    # Найти все файлы в папке и вложенных папках с сохранением структуры
    files = []
    for path in Path(folder_path).rglob("*"):
        if path.is_file():
            files.append(path)

    # Фильтрация файлов по расширению .py
    files = [f for f in files if f.suffix == '.py']

    # Создаем обертки для файлов
    file_wrappers = [FileWrapper(file) for file in files]

    # Анализ файлов
    files_data = await analyzer.analyze_files(files=file_wrappers)

    # Получение сводных данных
    summary = analyzer.get_summary()

    return files_data, summary
