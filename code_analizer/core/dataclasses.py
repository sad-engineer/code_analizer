#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class Entities:
    classes: list[str]
    functions: list[str]
    constants: list[str]


@dataclass
class CodeData:
    project_name: str
    lines_of_code: int
    comments: int
    empty_lines: int
    entities: Entities

    def __init__(self, project_name: str, lines_of_code: int, comments: int, empty_lines: int, classes: list[str], functions: list[str], constants: list[str]) -> None:
        self.project_name = project_name
        self.lines_of_code = lines_of_code
        self.comments = comments
        self.empty_lines = empty_lines
        self.entities = Entities(classes, functions, constants)

    
    