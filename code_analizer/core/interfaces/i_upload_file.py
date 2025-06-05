#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
from typing import Any, Protocol


class IUploadFile(Protocol):
    filename: str

    def read(self) -> Any: ...
