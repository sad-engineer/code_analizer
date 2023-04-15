#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog


class GUI:
    def __init__(self, master) -> None:
        """
        Инициализация GUI с переданным главным окном.

        :param master: экземпляр главного окна
        """
        self.master = master
        self.folder_path = ""
        self.select_folder_button = tk.Button(
            self.master,
            text="Select Project Folder",
            command=self.select_folder,
        )
        self.select_folder_button.pack()

    def select_folder(self) -> None:
        """
        Обработчик нажатия на кнопку "Select Project Folder". Открывает диалоговое окно выбора папки, запускает
        анализатор кода и выводит результаты анализа в консоль и файл.
        """
        self.folder_path = filedialog.askdirectory()
        self.master.destroy()
