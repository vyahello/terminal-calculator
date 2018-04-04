from abc import ABC, ABCMeta, abstractmethod
from functools import reduce
from typing import Union, Iterable


class Operation(ABC):
    """Represent abstraction for specific operation."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def perform(self) -> Union[int, float]:
        pass


class Add(Operation):
    """Represent add operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = numbers

    def perform(self) -> Union[int, float]:
        return reduce(lambda x, y: x + y, self._numbers)


class Subtract(Operation):
    """Represent subtract operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = numbers

    def perform(self) -> Union[int, float]:
        return reduce(lambda x, y: x - y, self._numbers)


class Multiply(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = numbers

    def perform(self) -> Union[int, float]:
        return reduce(lambda x, y: x * y, self._numbers)


class Divide(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = numbers

    def perform(self) -> float:
        return float('{:0.3f}'.format(reduce(lambda x, y: x / y, self._numbers)))
