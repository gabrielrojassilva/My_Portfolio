from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('roomate/<str:pk>',views.room, name="room"),
    path('living/',views.living, name="living")
]