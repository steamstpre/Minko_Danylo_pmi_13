import Validation
from Validation import *
from Collection import Collection
from TAX_FREE import Tax_free



our_path = "data_base.json"


def print_option():
    print("choose operation: 1 read from file , 2 input in file , 3 sort and kind of sort , 4 search , 5 edit , 6 delete , 7 exit")
    print("your operation:")
    operation = Validation.check_num_for_menu()
    return operation


def menu():
   while True:
    operation = print_option()
    if operation == 1:
        our_collection = Collection()
        our_collection.read_json(our_path)
        our_collection.__str__()
    if operation == 2:
            our_collection.input_to_obj(our_path)
    if operation == 3:
           sorted_arr = our_collection.sort()
    if operation == 4:
            serch_arr = our_collection.search()
    if operation == 5:
            our_collection.edit_elem(our_path)
    if operation == 6:
            our_collection.delete_elem_from_menu(our_path)
    if operation == 7:
            print("exit")
            break
    else:
        print("try corrcet num")










