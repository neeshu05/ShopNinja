from django.urls import path, include
from rest_framework import routers

from . import views 
#handle the api request
router = routers.DefaultRouter()

#register the views to api
router.register(r'',views.CategoryViewSet)
urlpatterns = [
    path('',include(router.urls))
]
