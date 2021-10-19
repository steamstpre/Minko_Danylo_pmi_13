from copy import deepcopy
from Validation import Validation
from Collection import Collection
from Memento import Memento

class CareTaker:
    def __init__(self , originator: Collection) -> None:
        self._mementos = []
        self._originator  = originator

    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(deepcopy(self._originator.save_momento()))

    def undo(self):
        if not len(self._mementos):
            return False

        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            state = memento.get_date()
            for item in state:
                print(item)

    def rendo(self):
        if not len(self._mementos):
            return False

        print("input number of n")
        our_n = Validation.check_num_for_menu()

        for i in range(len(self._mementos)):
            if i == our_n:
                self._originator.restore(self._mementos[i])




        #Опікун повинен знати, коли робити знімок творця та коли його потрібно відновлювати.
        # Опікун може зберігати історію минулих станів творця у вигляді стека знімків.
        # Коли треба буде скасувати останню операцію, він візьме «верхній» знімок зі стеку та передасть його творцеві для
        # відновлення.