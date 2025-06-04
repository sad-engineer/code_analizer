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
class CodeData:
    filename: str
    lines_of_code: int
    comments: int
    empty_lines: int
    entities: Entities

    def __init__(self, filename: str, lines_of_code: int, comments: int, empty_lines: int, classes: set[str], functions: set[str], constants: set[str]) -> None:
        self.filename = filename
        self.lines_of_code = lines_of_code
        self.comments = comments
        self.empty_lines = empty_lines
        self.entities = Entities(classes, functions, constants)

    
    