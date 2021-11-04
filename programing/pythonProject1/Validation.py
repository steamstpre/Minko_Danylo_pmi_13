from datetime import datetime
from VaccinationPointRequest import VaccinationPointRequest


class Validation:

    @staticmethod
    def check_name(func):
        def function_wrap(VaccinationPointRequest, value):
            if not isinstance(value, str):
                print("not correct name")
                raise ValueError
            res = func(VaccinationPointRequest, value)
            return res
        return function_wrap

    @staticmethod
    def check_point(func):
        def func_wrap(VaccinationPointRequest, value):
            if not (value == "Forum" or value == "VictoryGardens" or value == "KingCross"):
                print("not correct name of point")
                raise ValueError
            res = func(VaccinationPointRequest, value)
            return res
        return func_wrap

    @staticmethod
    def check_date(func):
        def func_wrap(VaccinationPointRequest, value):
            datetime.strptime(value, '%Y-%m-%d')
            if int(value[0:4]) > 2022:
                print("wrong data")
                raise ValueError
            res = func(VaccinationPointRequest, value)
            return res
        return func_wrap

    @staticmethod
    def check_time(func):
        def func_wrap(VaccinationPointRequest, value):
            try:
                if int(value[0:2]) < 10 or int(value[0:2]) > 18:
                    print("wrong data")
                    raise ValueError
            except:
                print("wrong value")
                raise ValueError
            res = func(VaccinationPointRequest, value)
            return res

        return func_wrap



