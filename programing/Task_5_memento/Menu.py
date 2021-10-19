import Validation
from Validation import *
from Collection import Collection
from TAX_FREE import Tax_free
from CareTaker import CareTaker

our_path = "data_base.json"

def print_option():
    print("choose operation: 1 read from file , 2 input in file , 3 sort and kind of sort , 4 search , 5 edit , 6 delete , 7 memento option , 8 exit")
    print("your operation:")
    operation = Validation.check_num_for_menu()
    return operation

def print_option_of_memento():
    print("choose operation of memento: 1 display all changes , 2 reboot state , 3 reboot n , 4 exit")
    print("your operation:")
    operation = Validation.check_num_for_menu()
    return operation

def menu_of_memento(careTaker):
    while True:
        operation = print_option_of_memento()
        if operation == 1:
            careTaker.show_history()
        if operation == 2:
            careTaker.undo()
        if operation == 3:
            careTaker.rendo()
        if operation == 4:
            print("exit")
            break


def menu():
   our_collection = Collection()
   our_collection.read_json(our_path)
   careTaker = CareTaker(our_collection)
   careTaker.backup()
   while True:
    operation = print_option()
    if operation == 1:
        our_collection.__str__()
    if operation == 2:
        our_collection.input_to_obj(our_path)
        careTaker.backup()
    if operation == 3:
        sorted_arr = our_collection.sort()
        Collection.print_arr(sorted_arr)
    if operation == 4:
        serch_arr = our_collection.search()
        Collection.print_arr(serch_arr)
    if operation == 5:
        our_collection.edit(our_path , careTaker)
        careTaker.backup()
    if operation == 6:
        our_collection.delete(our_path)
        careTaker.backup()
    if operation == 7:
        menu_of_memento(careTaker)
    if operation == 8:
        print("exit")
        break
    else:
        print("try corrcet num")










