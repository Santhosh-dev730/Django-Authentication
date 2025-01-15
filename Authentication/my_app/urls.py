from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/',home, name='home'),
    path('logout/',logout_view,name='logout')
]