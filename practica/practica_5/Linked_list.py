import Validation
from Const import Const
from Node import Node
import random


def generator(a, b):
    yield random.randint(a, b)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count_of_elements = 0

    def insert(self, data):
        our_node = Node(data)
        if (self.head):
            current_elem = self.head
            while (current_elem.next):
                current_elem = current_elem.next
            current_elem.next = our_node
            our_node.prev = current_elem
        else:
            self.head = our_node

    def __iter__(self):
        return self

    def __next__(self):
        if not self.head:
            raise StopIteration
        else:
            current_elem = self.head
            current_elem = current_elem.next
            return current_elem

    def print_list(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

    def get_list(self):
        arr = []
        current = self.head
        while (current):
            arr.append(current.data)
            current = current.next
        return arr

    def search_elem(self, data):
        current_elem = self.head
        if current_elem:
            while current_elem.next and current_elem.data != data:
                current_elem = current_elem.next
            if current_elem.data == data:
                return current_elem
            if current_elem.data != data:
                return False
        else:
            if current_elem == data:
                return current_elem
            else:
                return False

    def delete_elem(self, data):
        current_elem = self.head
        if current_elem:
            temp = None
            while current_elem.next and current_elem.data != data:
                temp = current_elem
                current_elem = current_elem.next
            if current_elem.data == data:
                temp.next = current_elem.next
        else:
            if current_elem == data:
                current_elem.data = None
            else:
                return False

    def get_count_of_elem(self):
        if (self.head):
            current_elem = self.head
            while (current_elem.next):
                self.count_of_elements += 1
                current_elem = current_elem.next
        return self.count_of_elements

    def apply_by_rand(self) -> None:
        print("diapazon n and m :")
        print("n: ")
        n = Validation.enter_num()
        print("m: ")
        m = Validation.enter_num()
        print("count of elements:")
        count_of_elements = Validation.enter_num()
        print("pos")
        pos = Validation.enter_num()

        for i in range(count_of_elements):
            self.insert_in_pos(generator(n, m) , pos)
            pos += 1

    def insert_in_pos(self , elem , pos):
        pos = pos - 1
        our_elem = Node(elem)
        if pos > self.get_count_of_elem() or pos < 0:
            print("wrong pos")
            return
        if pos == 0:
            self.head = our_elem
        else:
            index = 0
            current_elem = self.head
            while (current_elem.next):
                if index == pos:
                    current_elem.next = Node(elem , current_elem.next , current_elem)
                index += 1
                current_elem = current_elem.next

    def delete_index(self , i):
        current_elem = self.head
        index = 0
        if current_elem:
            temp = None
            while current_elem.next and index != i:
                temp = current_elem
                current_elem = current_elem.next
                index += 1
            if index == i:
                temp.next = current_elem.next
        else:
            if  index == i:
                current_elem.data = None
            else:
                return False

    def delete_from_n_to_m(self):
        print("diapazon n and m :")
        print("n: ")
        n = Validation.enter_num()
        print("m: ")
        m = Validation.enter_num()

        if n > self.get_count_of_elem() or n > m:
            raise ValueError('wrong val')
        for i in range(m - n + 1):
            self.delete_index(n)

