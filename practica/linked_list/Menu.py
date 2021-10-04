import Algorithm
import Validation
from Const import Const

def menu():
    while True:
        print("1 input by key ,2 input by random , 3 exit")
        operation = Validation.enter_num()
        if operation == Const.CONST_ONE:
            Algorithm.input_our_list()
        if operation == Const.CONST_TWO:
            Algorithm.generate_our_list()
        if operation == Const.CONST_THREE:
            break
        else:
            print("try 1 2 3")