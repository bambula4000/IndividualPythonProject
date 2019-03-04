from abc import ABC, abstractmethod
from typing import Any


class Requirement(ABC):
    @abstractmethod
    def passed(self, value: Any) -> bool:
        pass


class IsNumber(Requirement):
    def passed(self, value: Any) -> bool:
        return isinstance(value, int)


class IsBiggerThanZero(Requirement):
    def passed(self, value: Any)-> bool:
        return value > 0


class IsSmallerThanMillion(Requirement):
    def passed(self, value: Any)-> bool:
        return value < 1000000


class IsLongerThanOneSymbol(Requirement):
    def passed(self, value: Any)-> bool:
        return len(value) > 1


class CheckInputData(Requirement):
    def __init__(self, *requirements: Requirement):
        self._checks = requirements

    def passed(self, value: Any)-> bool:
        for requirement in self._checks:
            if not requirement.passed(value):
                print(f'{requirement.__class__.__name__} checks is failed. Enter correct data!')
                return False
        return True
