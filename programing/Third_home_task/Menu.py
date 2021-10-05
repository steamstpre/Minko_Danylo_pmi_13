import Validation
from Collection import Collection
from TAX_FREE import Tax_free
import Sort_by_date
import Search

our_path = "data_base.json"


def print_option():
    print("choose operation: 1 read from file , 2 input in file , 3 sort and kind of sort , 4 search , 5 edit , 6 delete , 7 exit")
    print("your operation:")
    operation = Validation.check_num_menu()
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
           sorted_arr = our_collection.sort(our_collection.input_field())
           Sort_by_date.print_arr(sorted_arr)
    if operation == 4:
            serch_arr = our_collection.search()
            Sort_by_date.print_arr(serch_arr)
    if operation == 5:
            our_collection.edit_elem(our_path)
    if operation == 6:
            our_collection.delete_elem_from_menu(our_path)
    if operation == 7:
            print("exit")
            break
<<<<<<< Updated upstream
    else:
        print("try corrcet num")
        operation = print_option()
=======
<<<<<<< Updated upstream
=======
    else:
        print("try corrcet num")
        
>>>>>>> Stashed changes




<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
>>>>>>> Stashed changes





