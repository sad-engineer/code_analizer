#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass
class Entities:
    classes: set[str]
    functions: set[str]
    constants: set[str]


@dataclass
class SummaryData:
    total_files: int
    total_lines_of_code: int
    total_comments: int
    total_empty_lines: int
    total_classes: int
    total_functions: int
    total_constants: int
    all_classes: set[str]
    all_functions: set[str]
    all_constants: set[str]


@dataclass
class CodeData:
    filename: str
    lines_of_code: int
    comments: int
    empty_lines: int
    entities: Entities
    file_content: str

    def __init__(
        self,
        filename: str,
        lines_of_code: int,
        comments: int,
        empty_lines: int,
        classes: set[str],
        functions: set[str],
        constants: set[str],
        file_content: str = "",
    ) -> None:
        self.filename = filename
        self.lines_of_code = lines_of_code
        self.comments = comments
        self.empty_lines = empty_lines
        self.entities = Entities(classes, functions, constants)
        self.file_content = file_content
