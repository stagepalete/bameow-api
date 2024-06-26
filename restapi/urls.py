"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views as products
from profiles import views as profiles
from reviews import views as reviews
from orders import views as orders

router = DefaultRouter()
router.register(r'api/v1/profile', profiles.UserViewSet, basename='profiles')
router.register(r'api/v1/login', profiles.LoginViewSet, basename='login')
router.register(r'api/v1/products', products.ProductsViewSet, basename='products')
router.register(r'api/v1/tokens', profiles.TokenIssuerViewSet, basename='tokens')
router.register(r'api/v1/reviews', reviews.ReviewViewSet, basename='reviews')
router.register(r'api/v1/adminorders', orders.AdminOrdersViewSet, basename='adminorders')
router.register(r'api/v1/orders', orders.UserOrdersViewSet, basename='userorders')

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/v1/logout/', profiles.LogoutView.as_view(), name='logout'),
]
