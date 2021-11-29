from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Const:
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

class Validation:
    @staticmethod
    def check_num(value):
        try:
            our_num = int(value)
        except:
            raise ValueError
        return our_num

    @staticmethod
    def check_vat_code(code):
        if not code[:Const.CONST_TWO] == "VA" and not code.check_num(code[Const.CONST_THREE:Const.CONST_SIX],
                                                        code[Const.CONST_SEVEN:Const.CONST_NINE],
                                                        code[Const.CONST_TEN:]) and not code[Const.CONST_TWO] == "-" and not \
                code[Const.CONST_SIX] == "-" and not code[Const.CONST_NINE] == "-":
            raise ValidationError(
            _('%(value)s is not correct code'),
            params={'value': code},
        )

    @staticmethod
    def check_vat_rate(value):
        if value < 0:
            raise ValidationError(
                _('%(value)s is not correct code'),
                params={'value': value}
            )