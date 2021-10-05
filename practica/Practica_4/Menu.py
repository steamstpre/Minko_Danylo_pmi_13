import Algorithm
import Validation
from Const import Const

def menu():
    global our_arr
    while True:
        print("1 input by key ,2 input by random , 3 print_arr , 4 algorithm , 5 exit")
        operation = Validation.enter_num()
        if operation == Const.CONST_ONE:
            our_arr =  Algorithm.input_our_list()
        if operation == Const.CONST_TWO:
            our_arr = Algorithm.rand_gener_our_list()
        if operation == Const.CONST_THREE:
            Algorithm.print_arr(our_arr)
        if operation == Const.CONST_FOUR:
            Algorithm.algoritm(our_arr)
        if operation == Const.CONST_FIVE:
            break
        else:
            print("try 1 2 3 4 5")
