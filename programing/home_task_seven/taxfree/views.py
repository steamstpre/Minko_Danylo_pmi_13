from collections import OrderedDict
from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .const import page_size_value, max_page_size_value
from .serializers import *
from .models import Tax_free
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
# Create your views here.
from .servises import ReadOnlyOrAdmin


class Pagenation_Tax(PageNumberPagination):
    page_query_param = "offset"
    page_size_query_param = "limit"
    page_size = page_size_value
    max_page_size = max_page_size_value



class TaxCreateView(generics.CreateAPIView):
    serializer_class = TaxFreeDetailSerializer

class TaxListView(generics.ListAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = [
        'id',
        'company',
        'vat_rate',
        'date_of_purchase',
        'vat_code',
        'date_of_tax_ref',
        'country',
    ]
    ordering_fields = '__all__'

    permission_classes = (IsAdminUser, )
    serializer_class = TaxFreeListSerializer
    queryset = Tax_free.objects.all()
    pagination_class = Pagenation_Tax


class TaxDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TaxFreeDetailSerializer
    queryset = Tax_free.objects.all()

