
class Const(object):
    CONST_ZERO = 0
    CONST_ONE = 1
    CONST_TWO = 2
    CONST_THREE = 3
    CONST_FOUR = 4
    CONST_FIVE = 5
    CONST_SIX = 6
    CONST_SEVEN = 7
    CONST_EIGHT = 8
    CONST_NINE = 9
    CONST_TEN = 10
    CONST_TWELVE = 12
    CONST_THIRTY_ONE = 31

def check_num_menu():
    try:
        our_num = int(input("enter num: "))
    except:
        print("try number")
        return check_num_menu()
    return our_num

def validation_of_vat_rate(vat_rate):
    vat_rate__ = int(vat_rate)
    if vat_rate__ >= 0 and vat_rate__ <= 40:
        return True
    else:
        print("not suitable rate")
        return False

def check_company(word):
    if any(char.isdigit() for char in word):
        print("number in string")
        #return check_alph(word)
        return False
    else:
        return True

def check_num(index_one , second_index , third_index):
    try:
        first_check = int(index_one)
        second_check = int(second_index)
        thir_check = int(third_index)
        return True
    except ValueError:
        print("wrong value")
        return False

def check_country(country):
    if country == "Germany" or  country == "Italy" or country == "France":
        return True
    else:
        print("not suitable counrty")
        return False

def check_data(data):
    day = int(data[:Const.CONST_THREE - Const.CONST_ONE])
    month = int(data[Const.CONST_THREE:Const.CONST_FIVE])
    year = int(data[Const.CONST_SIX:])

    if len(data) == Const.CONST_TEN and check_num(day, month, year):
         if data[Const.CONST_TWO] == "." and data[Const.CONST_FIVE] == "." :
            if  day != 0 and day < Const.CONST_THIRTY_ONE and day > Const.CONST_ZERO and month != 0 and  month <= Const.CONST_TWELVE and year > Const.CONST_ZERO :
                return True

def check_vat_code(code):
    if code[:Const.CONST_TWO] == "VA" and check_num(code[Const.CONST_THREE:Const.CONST_SIX], code[Const.CONST_SEVEN:Const.CONST_NINE] , code[Const.CONST_TEN:]) and code[Const.CONST_TWO] == "-" and code[Const.CONST_SIX] == "-" and code[Const.CONST_NINE] == "-":
        return True
