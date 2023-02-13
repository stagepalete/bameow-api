from django.urls import re_path 
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views
from products import views as pr
# router = DefaultRouter()
# router.register(r'profile', views.UserViewSet, basename='profiles')
# router.register(r'login', views.LoginViewSet, basename='login')
# router.register(r'products', pr.ProductsViewSet, basename='products')
urlpatterns = [
    # re_path(r'auth/login/', views.firstView.as_view(), name='auth1'), 
    # re_path(r'', include(router.urls))
]