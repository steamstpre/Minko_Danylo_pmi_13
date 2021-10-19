import Validation
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
    def company(self, value):
        if Validation.check_company(value):
            self._company = value
        else:
            print("try enter quality date")
            self._company = "none"
            return False
            #return False

    @vat_rate.setter
    def vat_rate(self, value):
        if Validation.validation_of_vat_rate(value):
            self._vat_rate = value
        else:
            self._vat_rate = "none"
            return False

    @country.setter
    def country(self, value):
        if Validation.check_country(value):
            self._country = value
        else:
            self._country = "none"
            return False

    @date_of_purchase.setter
    def date_of_purchase(self, value):
        if Validation.check_data(value):
            self._date_of_purchase = value
        else:
            self._date_of_purchase = "none"
            print("not date")
            return False

    @vat_code.setter
    def vat_code(self, value):
        if Validation.check_vat_code(value):
            self._vat_code = value
        else:
            self._vat_code = "none"
            print("wrong vat code")
            return False

    @date_of_tax_ref.setter
    def date_of_tax_ref(self, value):
        if Validation.check_data(value):
            self._date_of_tax_ref = value
        else:
            self._date_of_purchase = "none"
            print("not date")
            return False

    @id.setter
    def id(self, value):
        self._id = value

    def __str__(self):
        print(self.id , self.company , self.vat_rate, self.country , self.date_of_purchase , self.vat_code , self.date_of_tax_ref)
        return "0"

    def __eq__(self, second_object):
        return self.company.lower() == second_object.company.lower() and self.vat_rate == second_object.vat_rate and self.vat_code == second_object.vat_code and self.date_of_tax_ref == second_object.date_of_tax_ref and self.country == second_object.country and self.date_of_purchase == second_object.date_of_purchase and self.id == second_object.id

















