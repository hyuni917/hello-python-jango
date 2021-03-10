from django.urls import path
from . import views

urlpatterns = [
    path('write/', views.board_write),
    path('list/', views.boar_list),
]
