import abc
from Linked_list import LinkedList


class Strategy(abc):
    @abc.abstractmethod
    def generate_data(self, our_list:LinkedList):
        pass


class Strategy_one(Strategy):
    def generate_data(self, our_list:LinkedList):
        our_list.apply_by_rand()


class Strategy_two(Strategy):
    def generate_data(self, our_list):
        filename = "data.txt"
        with open(filename, "r") as file:
            for item in file:
                for x in item.split():
                    our_list.insert(int(x))
