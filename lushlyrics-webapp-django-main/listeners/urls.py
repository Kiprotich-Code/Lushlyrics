from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_listener, name="login"),
    path('register/', views.register_listener, name="register"),
    path('logout/', views.logout_listener, name="logout"),
]