#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
from pathlib import Path
from typing import Dict, List, Optional, Union

from code_analizer.core.code_text_analyzer import CodeAnalyzer
from code_analizer.core.line_processor import LineProcessor

# from code_analizer.output.factory import PrinterFactory


class CodeAnalyzerAPI:
    """
    API для анализа кода проекта.

    Пример использования:
    ```python
    api = CodeAnalyzerAPI()

    # Анализ проекта
    results = api.analyze_project("/path/to/project")

    # Получение статистики
    stats = api.get_statistics("/path/to/project")

    # Генерация отчета
    report = api.generate_report("/path/to/project", output_format="json")
    ```
    """

    def __init__(self):
        self.analyzer = None
        # self.output_handler = PrinterFactory()

    def analyze_project(self, project_path: Union[str, Path]) -> Dict:
        """
        Анализирует проект и возвращает результаты.

        Args:
            project_path: Путь к проекту для анализа

        Returns:
            Dict с результатами анализа
        """
        project_path = Path(project_path)
        self.analyzer = CodeAnalyzer(str(project_path), LineProcessor)
        self.analyzer.analyze()

        return {
            "project_name": self.analyzer.project_name,
            "statistics": {
                "lines_of_code": self.analyzer.lines_of_code,
                "comments": self.analyzer.comments,
                "empty_lines": self.analyzer.empty_lines,
                "classes": len(self.analyzer.classes),
                "functions": len(self.analyzer.functions),
                "constants": len(self.analyzer.constants),
            },
            "details": {
                "classes": list(self.analyzer.classes),
                "functions": list(self.analyzer.functions),
                "constants": list(self.analyzer.constants),
            },
        }

    def get_statistics(self, project_path: Union[str, Path]) -> Dict:
        """
        Возвращает статистику по проекту.

        Args:
            project_path: Путь к проекту

        Returns:
            Dict со статистикой
        """
        results = self.analyze_project(project_path)
        return results["statistics"]

    def generate_report(
        self,
        project_path: Union[str, Path],
        output_format: str = "json",
        output_path: Optional[Union[str, Path]] = None,
    ) -> Union[Dict, str]:
        """
        Генерирует отчет по проекту.

        Args:
            project_path: Путь к проекту
            output_format: Формат отчета ("json", "text", "html")
            output_path: Путь для сохранения отчета (опционально)

        Returns:
            Отчет в указанном формате
        """
        if not self.analyzer:
            self.analyze_project(project_path)

        if output_format == "json":
            return self.analyze_project(project_path)
        elif output_format == "text":
            return self.output_handler.format_text_report(self.analyzer)
        elif output_format == "html":
            return self.output_handler.format_html_report(self.analyzer)
        else:
            raise ValueError(f"Неподдерживаемый формат отчета: {output_format}")

    def get_project_structure(self, project_path: Union[str, Path]) -> List[Dict]:
        """
        Возвращает структуру проекта.

        Args:
            project_path: Путь к проекту

        Returns:
            List[Dict] со структурой проекта
        """
        project_path = Path(project_path)
        structure = []

        for path in project_path.rglob("*"):
            if path.is_file() and path.suffix == ".py":
                structure.append(
                    {"path": str(path.relative_to(project_path)), "type": "file", "size": path.stat().st_size}
                )
            elif path.is_dir() and not any(part.startswith(".") for part in path.parts):
                structure.append({"path": str(path.relative_to(project_path)), "type": "directory"})

        return structure
