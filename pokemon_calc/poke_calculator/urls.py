from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Pokemon-Calculator-Home'),
    path('export/', views.export, name='Pokemon-Calculator-Export'),
    path('select/', views.selectPoke, name='Pokemon-Calculator-Select')
]
