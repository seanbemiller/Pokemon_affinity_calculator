from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Pokemon-Calculator-Home'),
    path('export/', views.export, name='Pokemon-Calculator-Export'),
    path('select/', views.selectPoke, name='Pokemon-Calculator-Select'),
    path('swap/', views.swapPoke, name='Pokemon-Calculator-Swap'),
    path('find/', views.findPoke, name='Pokemon-Calculator-Find'),
    path('match/', views.matchPoke, name='Pokemon-Calculator-Match'),
    path('remove/', views.removePoke, name='Pokemon-Calculator-Remove')
]
