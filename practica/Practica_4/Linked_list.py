from Const import Const
from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count_of_elements = 0

    def insert(self , data):
        our_node = Node(data)
        if(self.head):
            current_elem = self.head
            while(current_elem.next):
                current_elem = current_elem.next
               # self.count_of_elements += Const.CONST_ONE
            current_elem.next = our_node
            our_node.prev = current_elem
        else:
            self.head = our_node

    def __iter__(self):
        if (self.head):
            current_elem = self.head
            current_elem = current_elem.next
            return current_elem
        else:
            return self.head

    def print_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def get_list(self):
        arr = []
        current = self.head
        while (current):
            arr.append(current.data)
            current = current.next
        return arr

    def search_elem(self , data):
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

    def delete_elem(self , data):
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


