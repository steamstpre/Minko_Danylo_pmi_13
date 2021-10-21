import Strategy
from Strategy import *

class Context:
    def __init__(self , operation_input = '0'):
        self.operation  = operation_input

    @property
    def operation(self):
        return self.operation

    @operation.setter
    def operation(self , value):
        self.operation = value

    def choose_strategy(self , our_list):
        if self.operation == '1':
            Strategy.Strategy_one.generate_data(our_list)
        if self.operation == '2':
            Strategy.Strategy_two.generate_data(our_list)