from abc import ABC, abstractmethod


class ValidatorInterface(ABC):
    @staticmethod
    @abstractmethod
    def validate(*, input: int) -> bool :
        pass