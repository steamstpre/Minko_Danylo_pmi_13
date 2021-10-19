import json
import Validation
from TAX_FREE import Tax_free
from Const import Const

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
        parametr = input("field:")
        try:
            sotred_list = sorted(self.our_list, key=lambda x: str(getattr(Tax_free, parametr)).lower())
            return sotred_list
        except:
            print("wrong field")

    def search(self):
        print("our search_elem:")
        search_elem = input("elem:")
        length = len(self.our_list)
        temp_arr = self.our_list
        res_arr = []
        for i in range(length):
            if (temp_arr[i].id == search_elem or temp_arr[i].date_of_purchase == search_elem or temp_arr[
                i].company == search_elem or temp_arr[i].country == search_elem or temp_arr[
                    i].date_of_tax_ref == search_elem or temp_arr[i].vat_code == search_elem or temp_arr[
                    i].vat_rate == search_elem) and i < length:
                res_arr.append(temp_arr[i])
        return res_arr

    def read_json(self , path):
         try:
            file_ = open(path , encoding="utf-8")
            file = json.load(file_)
            for i , item in enumerate(file):
                try:
                    our_obj = Tax_free()
                    our_obj.set_from_file(**item)
                    self.append(our_obj)
                except ValueError:
                    print("value errorr")
                    continue
                except AttributeError:
                    print("wrong atribute")
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
        try:
            count_of_fileds = int(input("count of fileds: "))
            if count_of_fileds > Const.CONST_SEVEN:
                raise ValueError
            for i in range(count_of_fileds):
                field = input("your field: ")
                value = input("your value: ")
                setattr(our_obj, field, value)
        except:
            print("wrong value")
        self.append(our_obj)
        self.write_to_json(path)

    def delete(self):
        id = input("your id: ")
        for i in self.our_list:
            if i._id == id:
                self.our_list.remove(i)

    def edit(self):
        id = input("your id: ")
        try:
            for i in self.our_list:
                if i._id == id:
                    attr = input("your field: ")
                    value = input("new value: ")
                    setattr(i, attr, value)
        except:
            print("smth wrong")


