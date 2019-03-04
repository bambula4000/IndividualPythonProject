from abc import ABC, abstractmethod
from typing import Any


class Input(ABC):
    @abstractmethod
    def value(self) -> Any:
        pass


class AskInput(Input):
    def __init__(self, question: str):
        self._question = question

    def value(self) -> Any:
        return input(f"{self._question} \n")


class AskIntInput(Input):
    def __init__(self, data: Input):
        self._data = data

    def value(self) -> int:
        while True:
            try:
                return int(self._data.value())
            except ValueError:
                print("Incorrect input. Please enter a digit")


class AskFloatInput(Input):
    def __init__(self, anyone: Input):
        self._anyone = anyone

    def value(self)-> float:
        while True:
            try:
                return float(self._anyone.value())
            except ValueError:
                print("Incorrect input. Please enter a float digit")


class InputCache(Input):
    def __init__(self, ask: Input):
        self._ask = ask
        self._data = []

    def value(self) -> Any:
        if not self._data:
            self._data.append(self._ask.value())
        return self._data[0]
