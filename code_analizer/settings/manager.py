#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
import os
from abc import ABC, abstractmethod
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


class DecimalConstructor(yaml.constructor.Constructor):
    """
    Конструктор YAML с поддержкой Decimal.
    """

    def construct_yaml_str(self, node):
        value = self.construct_scalar(node)
        try:
            return Decimal(value)
        except Exception:
            return value


class ConfigRepository(ABC):
    """Абстрактный класс для работы с конфигурацией"""

    @abstractmethod
    def load(self) -> Dict[str, Any]:
        """Загружает конфигурацию"""
        pass

    @abstractmethod
    def save(self, config: Dict[str, Any]) -> None:
        """Сохраняет конфигурацию"""
        pass


class YamlConfigRepository(ConfigRepository):
    """Реализация репозитория конфигурации для YAML файлов"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> Dict[str, Any]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                # Используем наш конструктор для поддержки Decimal
                yaml.add_constructor('tag:yaml.org,2002:str', DecimalConstructor.construct_yaml_str)
                return yaml.safe_load(file) or {}
        except FileNotFoundError:
            return {}

    def save(self, config: Dict[str, Any]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            # Преобразуем Decimal в строки при сохранении
            def decimal_representer(dumper, data):
                return dumper.represent_scalar('tag:yaml.org,2002:str', str(data))

            yaml.add_representer(Decimal, decimal_representer)
            yaml.dump(config, file, default_flow_style=False, allow_unicode=True)


class ConfigManager:
    """Менеджер конфигурации"""

    def __init__(self, repository: ConfigRepository, default_config: Dict[str, Any]):
        self.repository = repository
        self.default_config = default_config
        self._config: Optional[Dict[str, Any]] = None

    @property
    def config(self) -> Dict[str, Any]:
        """Получает текущую конфигурацию"""
        if self._config is None:
            self._config = self.repository.load()
            if not self._config:
                self._config = self.default_config
                self.repository.save(self._config)
        return self._config

    def get_setting(self, key_path: str) -> Any:
        """
        Получает значение настройки по ключу (вложенные ключи через точку).

        Parameters
        ----------
        key_path : str
            Путь к настройке через точку (например, "common.paths.for_reports")

        Returns
        -------
        Any
            Значение настройки

        Raises
        ------
        ValueError
            Если настройка не найдена
        """
        try:
            value = self.config
            for key in key_path.split("."):
                value = value[key]
            return value
        except (KeyError, TypeError):
            raise ValueError(f"Ошибка: настройка '{key_path}' не найдена.")

    def set_setting(self, key_path: str, new_value: Any) -> None:
        """
        Изменяет значение настройки и сохраняет его.

        Parameters
        ----------
        key_path : str
            Путь к настройке через точку
        new_value : Any
            Новое значение настройки
        """
        try:
            config = self.config
            keys = key_path.split(".")
            temp = config
            for key in keys[:-1]:
                temp = temp.setdefault(key, {})
            temp[keys[-1]] = new_value

            self.repository.save(config)
            self._config = config  # Обновляем кэш
            print(f"Настройка '{key_path}' изменена на {new_value}.")
        except Exception as e:
            print(f"Ошибка при изменении настройки: {e}")


def get_project_root():
    """Возвращает корневую директорию проекта"""
    # Если установлен как пакет, ищем директорию с pyproject.toml
    current = Path(__file__).resolve()
    while current.parent != current:  # Пока не достигли корня файловой системы
        if (current / 'pyproject.toml').exists():
            return current
        current = current.parent

    # Если не нашли pyproject.toml, возвращаем директорию с текущим файлом
    return Path(__file__).parent.parent.parent


# Определяем пути к конфигурационным файлам
PROJECT_ROOT = get_project_root()
CONFIG_DIR = PROJECT_ROOT / "settings"
if not CONFIG_DIR.exists():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
CONFIG_FILE = CONFIG_DIR / "code_analizer.yaml"

# Настройки по умолчанию
DEFAULT_CONFIG: Dict[str, Any] = {
    "details": "minimum",       # 'minimum', 'full'
    "file_suffix": [".py", ],
}

# Создаем экземпляр менеджера конфигурации
config_repository = YamlConfigRepository(str(CONFIG_FILE))
config_manager = ConfigManager(config_repository, DEFAULT_CONFIG)


# Функции для удобства использования
def get_setting(key_path: str) -> Any:
    """Получает значение настройки по ключу (вложенные ключи через точку)."""
    value = config_manager.get_setting(key_path)
    # Преобразуем строковые значения в Decimal при необходимости
    if isinstance(value, str) and value.replace('.', '').isdigit():
        return Decimal(value)
    return value


def set_setting(key_path: str, new_value: Any) -> None:
    """Изменяет значение настройки и сохраняет его в config.yaml."""
    # Преобразуем Decimal в строки при сохранении
    if isinstance(new_value, Decimal):
        new_value = str(new_value)
    config_manager.set_setting(key_path, new_value)


# Автоматическое создание файла конфигурации при первом запуске
if not os.path.exists(CONFIG_FILE):
    config_manager.repository.save(DEFAULT_CONFIG)
    print(f"Файл {CONFIG_FILE} создан с начальными настройками.")
