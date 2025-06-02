#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
"""
code_analizer - Пакет для анализа кода проекта.

Этот пакет предоставляет инструменты для анализа структуры кода,
поиска зависимостей и генерации отчетов о качестве кода.
"""

from .code_analyzer import CodeAnalyzer
from .config import create_config, delete_setting, get_config, get_setting, update_setting
from .guis import GUI
from .line_processor import LineProcessor
from .main import main
from .output_handlers import FileOutputHandler, OutputResultHandler, format_set

__all__ = [
    # Основные классы
    "CodeAnalyzer",
    "LineProcessor",
    "GUI",
    # Обработчики вывода
    "FileOutputHandler",
    "OutputResultHandler",
    "format_set",
    # Конфигурация
    "create_config",
    "get_config",
    "get_setting",
    "update_setting",
    "delete_setting",
    # Основные функции
    "main",
]
