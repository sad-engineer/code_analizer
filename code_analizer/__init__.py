#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
"""
code_analizer - Пакет для анализа кода проекта.

Этот пакет предоставляет инструменты для анализа структуры кода,
поиска зависимостей и генерации отчетов о качестве кода.
"""
from code_analizer.core import (
    CodeTextAnalyzer,
    FileBatchAnalyzer,
    LineProcessor,
    CodeData,
    SummaryData,
    IFormatter,
    IPrinter,
    IUploadFile,
    ConsoleFormatter,
    TextFormatter,
    JsonFormatter,
    HtmlFormatter,
    ConsoleSummaryFormatter,
    TextSummaryFormatter,
    JsonSummaryFormatter,
    HtmlSummaryFormatter,
    SUMMARY_FORMATTERS,
    CODE_FORMATTERS,
)
from code_analizer.output import (
    BasePrinter,
    ConsolePrinter,
    FilePrinter,
    JsonPrinter,
    OutputtingFactory,
    Outputting,
    PRINTERS,
)


__all__ = [
    "CodeTextAnalyzer",
    "FileBatchAnalyzer",
    "LineProcessor",
    "CodeData",
    "SummaryData",
    "IFormatter",
    "IPrinter",
    "IUploadFile",
    "ConsoleFormatter",
    "TextFormatter",
    "JsonFormatter",
    "HtmlFormatter",
    "ConsoleSummaryFormatter",
    "TextSummaryFormatter",
    "JsonSummaryFormatter",
    "HtmlSummaryFormatter",
    "SUMMARY_FORMATTERS",
    "CODE_FORMATTERS",
    "BasePrinter",
    "ConsolePrinter",
    "FilePrinter",
    "JsonPrinter",
    "OutputtingFactory",
    "Outputting",
    "PRINTERS",
]