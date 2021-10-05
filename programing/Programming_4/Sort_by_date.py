from TAX_FREE import Tax_free
from Validation import Const

def sort_by_date_of_purchase(data):

   length = len(data)
   for i in range(length):
       if i+1 < length and (int(data[i].date_of_purchase[Const.CONST_SIX:]) < int(data[i+1].date_of_purchase[Const.CONST_SIX:]) or int(data[i].date_of_purchase[Const.CONST_THREE:Const.CONST_FIVE]) < int(data[i+1].date_of_purchase[Const.CONST_THREE:Const.CONST_FIVE]) or int(data[i].date_of_purchase[:Const.CONST_THREE - Const.CONST_ONE]) < int(data[i+1].date_of_purchase[:Const.CONST_THREE - Const.CONST_ONE])) :
          temp = data[i]
          data[i] = data[i+1]
          data[i+1] = temp

   return data

def sort_by_tax_of_ref(data):
    length = len(data)
    for i in range(length):
        if i + 1 < length and (int(data[i].date_of_tax_ref[Const.CONST_SIX:]) < int(
                data[i + 1].date_of_tax_ref[Const.CONST_SIX:]) or int(
                data[i].date_of_tax_ref[Const.CONST_THREE:Const.CONST_FIVE]) < int(
                data[i + 1].date_of_tax_ref[Const.CONST_THREE:Const.CONST_FIVE]) or int(
                data[i].date_of_tax_ref[:Const.CONST_THREE - Const.CONST_ONE]) < int(data[i + 1].date_of_tax_ref[
                                                                                      :Const.CONST_THREE - Const.CONST_ONE])):
            temp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp

    return data

def print_arr(arr):
    try:
        for i in range(len(arr)):
            print(arr[i])
    except:
        print(arr)

