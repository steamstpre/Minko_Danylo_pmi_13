from Memento import Memento

class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state

    def get_date(self):
        return self._state

    def __str__(self):
        return [str(item) for item in self._state]

