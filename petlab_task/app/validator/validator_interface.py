from abc import ABC, abstractmethod


class ValidatorInterface(ABC):
    """
    This is a Interface all validator are to implemenet.
    """
    @staticmethod
    @abstractmethod
    def validate(**kwargs) -> bool :
        pass