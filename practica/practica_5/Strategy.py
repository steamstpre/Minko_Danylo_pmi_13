import abc
from Linked_list import LinkedList


class Strategy(abc):
    @abc.abstractmethod
    def generate_data(self, data: LinkedList, pos):
        pass


class Strategy_one(Strategy):
    def generate_data(self, data: LinkedList, pos):
        data.apply_by_rand()


class Strategy_two(Strategy):
    def generate_data(self, data: LinkedList, pos):
        filename = "data.txt"
        with open(filename, "r") as file:
            for item in file:
                for x in item.split():
                    data.insert(int(x))
