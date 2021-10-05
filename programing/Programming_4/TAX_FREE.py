from Validation import *
import json


class Tax_free(object):
    def __init__(self , **arr ):#id_input = "0" , company_input  = "none" , country_input = "none" , vat_rate_input = "0"  , date_of_purchase_input = "01.02.2020", vat_code_input = "VA123-12-123" ,  date_of_tax_ref_input="01.02.2020"):
        for (prop, default) in arr.items():
            setattr(self, prop, arr.get(prop, default))

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
    @check_company
    def company(self, value):
        self._company = value
            #return False

    @vat_rate.setter
    @validation_of_vat_rate
    def vat_rate(self, value):
        self._vat_rate = value


    @country.setter
    @check_country
    def country(self, value):
        self._country = value


    @date_of_purchase.setter
    @check_data
    def date_of_purchase(self, value):
        self._date_of_purchase = value

    @vat_code.setter
    @check_vat_code
    def vat_code(self, value):
        self._vat_code = value


    @date_of_tax_ref.setter
    @check_data
    def date_of_tax_ref(self, value):
        self._date_of_tax_ref = value


    @id.setter
    def id(self, value):
        self._id = value

    def __str__(self):
        print(self.id , self.company , self.vat_rate, self.country , self.date_of_purchase , self.vat_code , self.date_of_tax_ref)
        return "0"

    def __eq__(self, second_object):
        return self.company.lower() == second_object.company.lower() and self.vat_rate == second_object.vat_rate and self.vat_code == second_object.vat_code and self.date_of_tax_ref == second_object.date_of_tax_ref and self.country == second_object.country and self.date_of_purchase == second_object.date_of_purchase and self.id == second_object.id

















