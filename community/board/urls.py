from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.board_detail),
    path('write/', views.board_write),
    path('list/', views.boar_list),
]
