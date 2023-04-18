from django.urls import path
from .views import index, shop_detail

urlpatterns = [
    path('', index, name='index'),
    path('shop/<str:shop_id>', shop_detail, name='shop_detail'),
]