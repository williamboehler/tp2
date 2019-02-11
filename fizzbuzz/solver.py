# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Int2String(ABC):
    @abstractmethod
    def convert(self, number):
        pass  # pragma: no cover


class Displayer(ABC):
    @abstractmethod
    def display(self, string):
        pass  # pragma: no cover


class ProblemSolver:
    def __init__(self, converter, displayer):
        self.converter = converter
        self.displayer = displayer

    def solve(self, max):
        self.results = []
        for number in range(0, max):
            print('>>> %s ' % self.converter.convert(number+1))
            self.results.append(self.converter.convert(number+1))
        for result in self.results:
            self.displayer.display(result)
