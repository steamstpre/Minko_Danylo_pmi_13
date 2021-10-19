from Const import Const
from datetime import datetime

class Validation:

    @staticmethod
    def check_num(func):
        def function_wrap(Tax_free, value):
            if not isinstance(value, int):
                print("value must be int")
                raise ValueError
            res = func(Tax_free, value)
            return res
        return function_wrap

    @staticmethod
    def validation_of_vat_rate(func):
        def function_wrap(Tax_free, value):
            try:
                value = int(value)
            except:
                print("not int")
            if not value >= 0 and value <= 40:
                print("not correct vat rate")
                raise ValueError
            res = func(Tax_free, value)
            return res
        return function_wrap

    @staticmethod
    def check_company(func):
        def function_wrap(Tax_free, value):
            if not isinstance(value, str):
                print("not correct name of company")
                raise ValueError
            res = func(Tax_free, value)
            return res
        return function_wrap

    @staticmethod
    def check_country(func):
        def func_wrap(Tax_free, value):
            if not (value == "Germany" or value == "Italy" or value == "France"):
                print("not correct name of country")
                raise ValueError
            res = func(Tax_free, value)
            return res
        return func_wrap

    @staticmethod
    def check_vat_code(func):
        def func_wrap(Tax_free, value):
            try:
                a = int(value[Const.CONST_THREE:Const.CONST_SIX])
                b = int(value[Const.CONST_SEVEN:Const.CONST_NINE])
                c = int(value[Const.CONST_TEN:])
                if not (value[:Const.CONST_TWO] == "VA" and value[Const.CONST_TWO] == "-" and value[Const.CONST_SIX] == "-" and value[Const.CONST_NINE] == "-"):
                    print("not correct vat code")
                    raise ValueError
            except:
                print("not correct vat code")
                raise ValueError
            res = func(Tax_free, value)
            return res
        return func_wrap

    @staticmethod
    def check_date(func):
        def func_wrap(Tax_free , value):
            datetime.strptime(value, '%Y-%m-%d')
            if int(value[0:4]) > 2022:
                print("wrong data")
                raise ValueError
            res = func(Tax_free , value)
            return res
        return func_wrap

    @staticmethod
    def check_file(end=".json"):
        def validate_file(func):
            def validateFileNameExpl(L, filename):
                if not filename.endswith(end):
                    raise ValueError("wrong file")
                return func(L, filename)
            return validateFileNameExpl
        return validate_file

    @staticmethod
    def check_num_for_menu():
        try:
            our_num = int(input("enter num: "))
            return our_num
        except:
            print("try number")



