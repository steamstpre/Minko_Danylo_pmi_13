from django.contrib import admin
from django.urls import path , include
from taxfree.views import *


urlpatterns = [
    path('tax/create/' , TaxCreateView.as_view()),
    path('all/' , TaxListView.as_view()),
    path('tax/detail/<int:pk>/' , TaxDetailView.as_view()),
]
