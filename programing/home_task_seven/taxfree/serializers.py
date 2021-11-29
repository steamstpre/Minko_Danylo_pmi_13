from rest_framework import serializers
from taxfree.models import Tax_free

class TaxFreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax_free
        fields = ('id' , 'vat_rate' , 'date_of_purchase', 'vat_code','date_of_tax_ref','country')

class TaxFreeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax_free
        fields = '__all__'

