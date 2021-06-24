from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('symbols', views.symbols, name='symbols'),
]