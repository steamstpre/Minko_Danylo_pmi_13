from Validation import Validation
import json


class Tax_free(object):
    def __init__(self , id_input = "0", companu_input  = "none" , country_input = "none" , vat_rate_input = "0" ,  date_of_purchase_input = "2003-03-23" , vat_code_input = "VA-000-00-000" , date_of_tax_ref_input = "2003-03-23"):
        self._id = id_input
        self._company = companu_input
        self._country = country_input
        self._vat_rate = vat_rate_input
        self._date_of_purchase = date_of_purchase_input
        self._vat_code = vat_code_input
        self._date_of_tax_ref = date_of_tax_ref_input


    @property
    def id(self):
        return self._id

    @property
    def company(self):
        return self._company

    @property
    def country(self):
        return self._country

    @property
    def vat_rate(self):
        return self._vat_rate

    @property
    def date_of_purchase(self):
        return self._date_of_purchase

    @property
    def vat_code(self):
        return self._vat_code

    @property
    def date_of_tax_ref(self):
        return self._date_of_tax_ref

    @company.setter
    @Validation.check_company
    def company(self, value):
        self._company = value


    @vat_rate.setter
    @Validation.validation_of_vat_rate
    def vat_rate(self, value):
        self._vat_rate = value


    @country.setter
    @Validation.check_country
    def country(self, value):
        self._country = value


    @date_of_purchase.setter
    @Validation.check_date
    def date_of_purchase(self, value):
        self._date_of_purchase = value

    @vat_code.setter
    @Validation.check_vat_code
    def vat_code(self, value):
        self._vat_code = value


    @date_of_tax_ref.setter
    @Validation.check_date
    def date_of_tax_ref(self, value):
        self._date_of_tax_ref = value


    @id.setter
    def id(self, value):
        self._id = value

    def set_from_file(self , **arr):
        for (field, value) in arr.items():
            setattr(self, field, value)

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in dir(self) if
                     not name.startswith('_'))

    def __str__(self):
        return "Company:" + '\n'.join("%s : %r" % (key, str(val)) for (key, val)
                                        in self.__get_dictionary().items()) + " "



















