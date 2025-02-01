# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
   # path('chat/<str:username>/', views.chat, name='chat_room'),
    path('chat/<str:username>/', views.chat_room, name='chat_room'),
    path('account/',views.account,name='account'),
    #path('profile/change_picture/', views.change_profile_picture, name='change_profile_picture'),
]
