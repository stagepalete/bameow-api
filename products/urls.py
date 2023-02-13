from django.urls import re_path 
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# # router.register('profile', views.UserViewSet)
# router.register(r'products', views.ProductsViewSet, basename='products')

# urlpatterns = [
#     re_path(r'', include(router.urls))
# ]