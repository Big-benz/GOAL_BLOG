from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<str:pk>", views.blog, name= "blog"),
    path('room',views.room, name='room'),
    path('new-room', views.new_room, name = 'new_room'),
    path('new-room/<str:room>/', views.chat_room, name='chat_room'),
    path('checkroom', views.checkroom, name='checkroom'),
    path('send', views.send, name = 'send'),
    path('receivemessages/<str:room>/', views.receivemessages, name='receivemessages'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),



]


