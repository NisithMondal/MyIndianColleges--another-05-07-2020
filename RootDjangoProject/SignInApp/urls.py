from django.urls import path
from . import views
urlpatterns = [
    path('sign-in/', views.signIn),
    path('login/', views.login),
    path('logout/', views.logout),
]