
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

def check_num(func):
   def function_wrap(self , value):
       if not isinstance(value , int):
           raise Exception("value must be int".format(func.__name__))
       res = func(self , value)
       return res
   return function_wrap


def validation_of_vat_rate(func):
    def function_wrap(self , value):
        if not (( isinstance(value , int)) and (value >= 0 and value <= 40)):
            raise Exception("not correct vat rate".format(func.__name__))
        res = func(self , value)
        return res
    return function_wrap

def check_company(func):
    def function_wrap(self , value):
        if not isinstance(value , str):
            raise Exception("not correct name of company".format(func.__name__))
        res = func(self , value)
        return res
    return function_wrap


def check_date(index_one , second_index , third_index):
    try:
        first_check = int(index_one)
        second_check = int(second_index)
        thir_check = int(third_index)
        return True
    except ValueError:
        print("wrong value")
        return False

def check_country(func):
    def func_wrap(self , value):
        if not(value == "Germany" or  value == "Italy" or value == "France"):
            raise Exception("not coerrect country".format(func.__name__))
        res = func(self , value)
        return res
    return func_wrap


def check_data(func):
    def func_wrap(self , value):
        try:
            day = int(value[:Const.CONST_THREE - Const.CONST_ONE])
            month = int(value[Const.CONST_THREE:Const.CONST_FIVE])
            year = int(value[Const.CONST_SIX:])
        except:
            print("not a date")
            value = "none"
            res = func(self , value)
            return res
        if not len(value) == Const.CONST_TEN:
            if not value[Const.CONST_TWO] == "." and value[Const.CONST_FIVE] == "." :
                if not day != 0 and day < Const.CONST_THIRTY_ONE and day > Const.CONST_ZERO and month != 0 and  month <= Const.CONST_TWELVE and year > Const.CONST_ZERO :
                    raise Exception("not corrcet data".format(func.__name__))
        res = func(self, value)
        return res
    return func_wrap

def check_vat_code(func):
    def func_wrap(self , value):
        if not(value[:Const.CONST_TWO] == "VA" and check_date(value[Const.CONST_THREE:Const.CONST_SIX], value[Const.CONST_SEVEN:Const.CONST_NINE] , value[Const.CONST_TEN:]) and value[Const.CONST_TWO] == "-" and value[Const.CONST_SIX] == "-" and value[Const.CONST_NINE] == "-"):
            raise Exception("not correct data".format(func.__name__))
        res = func(self , value)
        return res
    return func_wrap

def check_num_for_menu():
    try:
        our_num = int(input("enter num: "))
    except:
        print("try number")
        return check_num_for_menu()
    return our_num
