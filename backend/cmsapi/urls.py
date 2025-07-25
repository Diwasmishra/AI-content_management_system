# cmsapi/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CategoryViewSet, ArticleViewSet

router = DefaultRouter()

router.register(r'articles', ArticleViewSet, basename='article')

router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
