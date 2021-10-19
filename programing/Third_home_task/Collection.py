import json
import Search
import Sort_by_date
import Validation
from TAX_FREE import Tax_free

class Collection(object):

    def __init__(self , *our_list):
        self.our_list = list(our_list[:])

    def __getitem__(self, item):
        return self.our_list[item]

    def __len__(self):
        return len(self.our_list)

    def __setitem__(self, key, value):
        self.our_list[key] = value

    def __str__(self):
        return [str(item) for item in self.our_list]

    def append(self , item):
        self.our_list.append(item)

    def sort(self , parametr="field"):
        if parametr == "_date_of_purchase" or parametr == "_date_of_tax_ref":
            sorted_list = Sort_by_date.sort_by_date_of_purchase(self.our_list)
        else:
            sotred_list = sorted(self.our_list , key=lambda x: str(getattr(Tax_free , parametr)).lower())
        return sotred_list

    def search(self):
        print("our search_elem:")
        elem = input("elem:")
        res =  Search.search(self.our_list , search_elem=elem)
        return res

    def read_json(self , path):
        try:
            file_ = open(path , encoding="utf-8")
            file = json.load(file_)
            for i , item in enumerate(file):
                try:
                    self.our_list.append(Tax_free(**item))
                except ValueError:
                    print("error")
                    continue
            file_.close()
        except:
            print("not correct data")

    def write_to_json(self , path):
        with open(path , 'w' , encoding='utf-8') as our_file:
            json.dump([obj.__dict__ for obj in self.our_list], our_file , ensure_ascii=False)
        our_file.close()


    def input_to_obj(self , path):
        our_obj = Tax_free()
        print("id: ")
        id = Validation.check_num_menu()
        our_obj.id = id
        company_name = str(input("your name: "))
        our_obj.company = company_name
        country  = str(input("your country: "))
        our_obj.country = country
        vat_rate = input("var rate")
        our_obj.vat_rate = vat_rate
        date_of_purchase = str(input("your date of purchase: "))
        our_obj.date_of_purchase = date_of_purchase
        vat_code = input("vat code:")
        our_obj.vat_code = vat_code
        date_of_tax_ref = input("date of tax ref:")
        our_obj.date_of_tax_ref = date_of_tax_ref
        self.append(our_obj)
        self.write_to_json(path)

    @staticmethod
    def input_field():
        print("please choose fieild: 1 id , 2 comapny , 3 country , 4 vat rate , 5 date of purchase , 6 vat code , 7 date of tax ref")
        our_operation = Validation.check_num_menu()
        while True:
            if our_operation == 1:
                return "id"
            if our_operation == 2:
                return "company"
            if our_operation == 3:
                return "country"
            if our_operation == 4:
                return "vat_rate"
            if our_operation == 5:
                return "date_of_purchase"
            if our_operation == 6:
                return "vat_code"
            if our_operation == 7:
                return "date_of_tax_ref"
            else:
                print("please try 1-7")
                our_operation = Validation.check_num_menu()

    def delete_obj(self , obj):
        self.our_list.remove(obj)

    def delete_elem_from_menu(self , path):
        arr_of_search_element = self.search()
        print("enter index of elelm")
        index = Validation.check_num_menu()
        while True:
            if index < len(arr_of_search_element):
                print(arr_of_search_element[index])
                self.our_list.remove(arr_of_search_element[index])
                self.write_to_json(path)
                break
            else:
                print("try correct index")
                index = Validation.check_num_menu()

    def edit_elem(self , path):
        arr_of_search_element = self.search()
        Sort_by_date.print_arr(arr_of_search_element)
        print("enter index of elelm")
        index = Validation.check_num_menu()
        while True:
            if index < len(arr_of_search_element):
                print(arr_of_search_element[index])
                self.our_list.remove(arr_of_search_element[index])
                res = self.input_field()
                new_filed = input("new parametr:")
                setattr(arr_of_search_element[index] , res , new_filed)
                self.our_list.append(arr_of_search_element[index])
                self.write_to_json(path)
                break
            else:
                print("try correct index")
                index = Validation.check_num_menu()


