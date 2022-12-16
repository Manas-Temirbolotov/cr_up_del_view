from rest_framework import routers

# from . import views
from django.urls import path
from item import views
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet, FirmaSerializer, CategoryDetailAPIView, CategoryAPIView

router = DefaultRouter()
router.register('item', ItemViewSet)


urlpatterns = [
    path('api/item/', views.ItemViewSet.as_view({'get': 'list'}), name = 'item'),
    path('firma/', views.firma_view, name = 'firma_list'),
    path('firma/<int:id>/', views.firma_detail, name = 'firma_detail'),
    path('category/', views.CategoryAPIView, name = 'category'),
    path('category/', views.CategoryDetailAPIView, name = 'category'),
    # path('category/<int:id>/', views.CategoryDetailAPIView.as_view(), name ='category_detail'),



]