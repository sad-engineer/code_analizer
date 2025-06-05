#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.core.formatters.console import ConsoleFormatter, ConsoleSummaryFormatter
from code_analizer.core.formatters.html import HtmlFormatter, HtmlSummaryFormatter
from code_analizer.core.formatters.json import JsonFormatter, JsonSummaryFormatter
from code_analizer.core.formatters.text import TextFormatter, TextSummaryFormatter

CODE_FORMATTERS = {"console": ConsoleFormatter, "text": TextFormatter, "json": JsonFormatter, "html": HtmlFormatter}
SUMMARY_FORMATTERS = {
    "console": ConsoleSummaryFormatter,
    "text": TextSummaryFormatter,
    "json": JsonSummaryFormatter,
    "html": HtmlSummaryFormatter,
}

__all__ = [
    "BaseFormatter",
    "ConsoleFormatter",
    "TextFormatter",
    "JsonFormatter",
    "HtmlFormatter",
    "ConsoleSummaryFormatter",
    "TextSummaryFormatter",
    "JsonSummaryFormatter",
    "HtmlSummaryFormatter",
    "CODE_FORMATTERS",
    "SUMMARY_FORMATTERS",
]
