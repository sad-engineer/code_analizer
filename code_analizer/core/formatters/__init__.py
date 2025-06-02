#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from code_analizer.core.formatters.base import BaseFormatter
from code_analizer.core.formatters.console import ConsoleFormatter
from code_analizer.core.formatters.html import HtmlFormatter
from code_analizer.core.formatters.json import JsonFormatter
from code_analizer.core.formatters.text import TextFormatter

__all__ = ["BaseFormatter", "ConsoleFormatter", "TextFormatter", "JsonFormatter", "HtmlFormatter"]

FORMATTERS = {"console": ConsoleFormatter, "text": TextFormatter, "json": JsonFormatter, "html": HtmlFormatter}
