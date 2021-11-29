from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Tax_free
# Create your views here.

class TaxCreateView(generics.CreateAPIView):
    serializer_class = TaxFreeDetailSerializer

class TaxListView(generics.ListAPIView):
    serializer_class = TaxFreeListSerializer
    queryset = Tax_free.objects.all()

class TaxDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaxFreeDetailSerializer
    queryset = Tax_free.objects.all()
