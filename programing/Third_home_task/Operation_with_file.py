import Validation
from TAX_FREE import Tax_free
import Search
import pickle
import os
import _json

def input(company , way_to_file):
    try:
        file = open(way_to_file , "wb")
        try:
            pickle.dump(company , file)
        finally:
            file.close()
    except FileNotFoundError:
        print("not found file")

def read(way_to_file):
    try:
        file = open(way_to_file, "rb")
        try:
            data_base = pickle.load(file)
            return data_base
        finally:
            file.close()
    except FileNotFoundError:
        print("not found file")

def delete_from_data_base(way_to_file , indetificator):
    our_arr = read(way_to_file)
    delete_items = Search.search(our_arr , indetificator)
    res_arr = []
    for i in range(len(our_arr)):
        for j in range(len(delete_items)):
            if our_arr[i] != delete_items[j]:
                res_arr.append(our_arr[i])
    os.remove(way_to_file)
    input(res_arr , way_to_file)

def editing(way_to_file , indetificator):
    our_arr = read(way_to_file)
    edit_item = Search.search(our_arr, indetificator)
    for i in range(len(edit_item)):
        print(edit_item[i])
    item = int(input("Which item you wanna edit? "))
    if item < len(edit_item):
        our_item = edit_item[item]
        kind_of_editing = input("Which field you wanna edit? ")
        if kind_of_editing == "name of company":
            new_item = input("new name")
            if Validation.check_company(new_item):
                delete_from_data_base(way_to_file, our_item)
                our_item.company = new_item
                input(our_item , way_to_file)
            else:
                print("enter another name of company:")
                Validation.check_company(new_item)
        if kind_of_editing == "Country":
            new_item = input("new Country")
            if Validation.check_country(new_item):
                delete_from_data_base(way_to_file, our_item)
                our_item.country = new_item
                input(our_item , way_to_file)
            else:
                print("enter another country:")
                new_item = input("new Country")
                Validation.check_country(new_item)
        if kind_of_editing == "data of purchase":
            new_item = input("new data of purchase: ")
            if Validation.check_data(new_item):
                delete_from_data_base(way_to_file, our_item)
                our_item.date_of_purchase = new_item
                input(our_item , way_to_file)
            else:
                print("enter another date:")
                new_item = input("new date")
                Validation.check_data(new_item)
    else:
        print("please try correct num")








