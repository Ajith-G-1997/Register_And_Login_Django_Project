from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='homepage'),
    path('register/',views.Register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.Logout,name='logout')
]