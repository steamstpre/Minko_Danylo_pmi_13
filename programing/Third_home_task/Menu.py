import Validation
from TAX_FREE import Tax_free
import Operation_with_file
import Sort
import Search


def menu():
    print("choose operation: 1 read from file , 2 input in file , 3 sort and kind of sort , 4 search , 5 delete , 6 edit file , 7 exit")
    print("your operation:")
    operation = Validation.check_num_menu()
    way_to_file = "data_base.bin"
    while True:
        if operation == 1:
            arr = Operation_with_file.read("data_base.bin")
            Sort.print_arr(arr)
            print("your operation:")
            operation = Validation.check_num_menu()
        if operation == 2:
                id = str(input("your id: "))
                company_name = str(input("company name: "))
                vat_rate = str(input("vat rate: "))
                country = str(input("country: "))
                date_of_purchase = str(input("date_of_purch: "))
                vat_code = str(input("vat code :"))
                date_of_tax_ref = str(input("date of tax ref: "))
                try:
                    our_company = Tax_free(id_input=id , company_input=company_name , vat_rate_input=vat_rate , country_input=country , date_of_purchase_input=date_of_purchase , vat_code_input=vat_code , date_of_tax_ref_input=date_of_tax_ref)
                except:
                    print("not  valid data")
                Operation_with_file.input(our_company , way_to_file)
                print("your operation:")
                operation = Validation.check_num_menu()
        if operation == 3:
            print("kind of sort 1 comapany name , 2 vat rate , 3 country , 4 date of purchase , 5 date of tax ref , 6 exit")
            kind_of_sort = Validation.check_num_menu()
            our_arr = Operation_with_file.read(way_to_file)
            while True:
                if kind_of_sort == 1:
                    our_arr = Sort.sort_by_company(our_arr)
                    Sort.print_arr(our_arr)
                    kind_of_sort = Validation.check_num_menu()
                    break
                if kind_of_sort == 2:
                    our_arr = Sort.sort_by_vat_rate(our_arr)
                    Sort.print_arr(our_arr)
                    kind_of_sort = Validation.check_num_menu()
                if kind_of_sort == 3:
                    our_arr = Sort.sort_by_country(our_arr)
                    Sort.print_arr(our_arr)
                    kind_of_sort = Validation.check_num_menu()
                if kind_of_sort == 4:
                    our_arr = Sort.sort_by_date_of_purchase(our_arr)
                    Sort.print_arr(our_arr)
                    kind_of_sort = Validation.check_num_menu()
                if kind_of_sort == 5:
                    our_arr = Sort.sort_by_tax_of_ref(our_arr)
                    Sort.print_arr(our_arr)
                    kind_of_sort = Validation.check_num_menu()
                if kind_of_sort == 6:
                    break
            print("your operation:")
            operation = Validation.check_num_menu()
        if operation == 4:
            while True:
                print("search: ")
                search_elem = input("your num: ")
                our_arr = Operation_with_file.read(way_to_file)
                our_elemets = Search.search(our_arr, search_elem)
                if len(our_elemets) == 0:
                    print("not found")
                    print("your operation:")
                    operation = Validation.check_num_menu()
                    break
                print("our res:")
                Sort.print_arr(our_elemets)
                print("Continue? yes or no")
                continue__ = input(":")
                if continue__ == "yes":
                    continue
                elif continue__ == "no":
                    print("your operation:")
                    operation = Validation.check_num_menu()
                    break
        if operation == 5:
            while True:
                print("element which you wanna delete")
                elem = input("elem:")
                our_arr = Operation_with_file.read(way_to_file)
                try:
                     length = len(our_arr)
                except:
                     length = 0
                if length == 0:
                    print("404")
                    Sort.print_arr(our_arr)
                    print("your operation:")
                    operation = Validation.check_num_menu()
                    break
                else:
                    Operation_with_file.delete_from_data_base(way_to_file , elem)
                    print("your operation:")
                    operation = Validation.check_num_menu()
                    break
        if operation == 6:
            while True:
                print("which elem you wanna edit:")
                edit_elem = input("your elem:")
                our_arr = Operation_with_file.read(way_to_file)
                res_arr = Search.search(our_arr , edit_elem)
                if len(res_arr) == 0:
                    print("404")
                    print("your operation:")
                    operation = Validation.check_num_menu()
                    break
                else:
                    Operation_with_file.editing(way_to_file , edit_elem)
                    print("your operation:")
                    operation = Validation.check_num_menu()
                    break
        if operation == 7:
            break





