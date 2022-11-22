# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: ChemAdd.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 11/21/22 21:17
"""


class ChemAdd:
    """
    add a chemical to the database
    """

    def __init__(self, code: str | None, cas: str | None, name: str, weight: float | None, remaining: int):
        self.code = code
        self.cas = cas
        self.name = name
        self.weight = weight
        if remaining < 0 or remaining > 5:
            remaining = 0
        self.remaining = remaining

    def add(self):
        """
        add a chemical to the database
        :return: None
        """

