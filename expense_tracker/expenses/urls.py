from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from expenses import views

urlpatterns = [
    path('',views.index, name='home'),
    path('category/',include('expenses.category.urls')),
    path('product/',include('expenses.product.urls'))
]