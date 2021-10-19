from abc import abstractmethod

class Memento:
    @abstractmethod
    def get_date(self) -> str:
        pass
