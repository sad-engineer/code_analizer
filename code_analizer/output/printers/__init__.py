#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from code_analizer.output.printers.base import BasePrinter
from code_analizer.output.printers.console import ConsolePrinter
from code_analizer.output.printers.file import FilePrinter
from code_analizer.output.printers.json import JsonPrinter

__all__ = ["BasePrinter", "ConsolePrinter", "FilePrinter", "JsonPrinter"]

PRINTERS = {"console": ConsolePrinter, "file": FilePrinter, "json": JsonPrinter}
