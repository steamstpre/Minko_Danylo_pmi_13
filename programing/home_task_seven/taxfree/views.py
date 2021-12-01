from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Tax_free
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TaxCreateView(generics.CreateAPIView):
    serializer_class = TaxFreeDetailSerializer

class TaxListView(generics.ListAPIView):
    serializer_class = TaxFreeListSerializer
    queryset = Tax_free.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('company' ,'vat_rate','date_of_purchase','vat_code','date_of_tax_ref','country')
    # filter_fields = ('id' , 'vat_rate' , 'date_of_purchase','vat_code','date_of_tax_ref','country','company')


class TaxDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaxFreeDetailSerializer
    queryset = Tax_free.objects.all()

class TaxSortView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaxFreeDetailSerializer
    queryset = Tax_free.objects.all()
