#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
from pathlib import Path

from code_analizer.core.interfaces.upload_file import IUploadFile


class FileWrapper(IUploadFile):
    """Класс-обертка для работы с файлами"""

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.filename = str(file_path)
        self._content = None

    async def read(self) -> bytes:
        """Читает содержимое файла"""
        if self._content is None:
            with open(self.file_path, 'rb') as f:
                self._content = f.read()
        return self._content
