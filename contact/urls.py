from django.urls import path
from .views import *

urlpatterns = [
    path('',indexview,name='home'),
    path('signup/',SignUp,name='signup'),
    path('login/',Login,name='login'),
    path('logout/',LogOut,name='logout'),
    path('choose/',ChooseView,name='choose'),
    path('info/<str:name>/',InfoView,name='info'),
]
