from msilib.schema import Patch
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes), 
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
# 6.18de kaldın

]