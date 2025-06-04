#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Protocol, Any


class IUploadFile(Protocol):
    filename: str
    def read(self) -> Any: ...
