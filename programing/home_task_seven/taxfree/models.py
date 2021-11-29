from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from .validation import Validation

User = get_user_model()

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only letters.')
# Create your models here.
class Tax_free(models.Model):
    company = models.CharField(verbose_name='company' , db_index=True,  max_length=64 , validators=[alphanumeric])
    vat_rate = models.IntegerField(verbose_name='vat_rate',  max_length=40, db_index=True , validators=[Validation.check_vat_rate])
    date_of_purchase = models.DateTimeField(verbose_name='date_of_purchase', db_index=True , max_length=10)
    vat_code = models.CharField(verbose_name='vat_code', db_index=True , validators=[Validation.check_vat_code] , max_length=13 , unique=True)
    date_of_tax_ref = models.DateTimeField(verbose_name='date_of_tax_ref', db_index=True,max_length=10)
    COUNTRY_TYPES = (
        (1 , 'Germany'),
        (2, 'Italy'),
        (3, 'France'),
    )
    country = models.IntegerField(verbose_name='country', choices=COUNTRY_TYPES)
    user = models.ForeignKey(User , verbose_name='User' , on_delete=models.CASCADE)