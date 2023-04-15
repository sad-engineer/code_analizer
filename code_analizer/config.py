#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
import configparser
import os
import codecs


CONFIG_PATH = 'settings.ini'

   
def create_config():
    """ Создает файл конфигураций """
    config = configparser.ConfigParser()
    # Общие настройки
    config.add_section("Global settings")
    # Показатель структуры отчета: 'minimum' - только количество, 'full' - количество и состав
    config.set("Global settings", "details", "minimum")    # 'minimum', 'full'

    with codecs.open(CONFIG_PATH, "w", "utf8") as config_file:
        config.write(config_file)
 
    
def get_config():
    """ Возвращает объект прочитанного файла настроек """
    if not os.path.exists(CONFIG_PATH):
        create_config()
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8')
    return config
 
 
def get_setting(section, setting):
    """ Получает настройку """
    config = get_config()
    value = config.get(section, setting)
    return value
 
 
def update_setting(section, setting, value):
    """ Обновляет настройку """
    config = get_config()
    config.set(section, setting, value)
    with codecs.open(CONFIG_PATH, "w", "utf8") as config_file:
        config.write(config_file)
 
 
def delete_setting(section, setting):
    """ Удаляет настройку """
    config = get_config()
    config.remove_option(section, setting)
    with codecs.open(CONFIG_PATH, "w", "utf8") as config_file:
        config.write(config_file)
