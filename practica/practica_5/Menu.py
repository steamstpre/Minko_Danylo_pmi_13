import Validation
from Strategy import Strategy , Strategy_one , Strategy_two
from Linked_list import LinkedList
from Context import Context


def message():
    print("choose strategy : Strategy one 1, Strategy two 2  , Delete elem 3  , Search elem 4 , print list 5 , insert 6 , delete elem from n to m 7 , exit 8")
    operation = Validation.enter_num()
    return operation

def strategy_input(operation , our_list , context):
    context.operation = operation
    context.choose_strategy(our_list)

def menu():
    operation = message()
    our_list = LinkedList()
    context = Context()
    while True:
        if operation == 1:
            strategy_input(operation , our_list , context)
        if operation == 2:
            strategy_input(operation, our_list, context)
        if operation == 3:
            our_elem = Validation.enter_num()
            our_list.delete_elem(our_elem)
        if operation == 4:
            our_elem = Validation.enter_num()
            our_list.search_elem(our_elem)
        if operation == 5:
            our_list.print_list()
        if operation == 6:
            our_elem = Validation.enter_num()
            our_list.insert(our_elem)
        if operation == 7:
            our_list.delete_from_n_to_m()
        if operation == 8:
            print("exit")
            break



