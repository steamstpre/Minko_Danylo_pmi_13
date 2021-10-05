class Node:
    def __init__(self, data = None , next = None , prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    #
    # @property
    # def data(self):
    #     return self.data
    # @property
    # def next(self):
    #     return self.next
    #
    # @data.setter
    # def data(self , data__):
    #     self.data =  data__
    # @next.setter
    # def next(self , node):
    #     self.next = node
    #
    # def __repr__(self):
    #     return self.data
