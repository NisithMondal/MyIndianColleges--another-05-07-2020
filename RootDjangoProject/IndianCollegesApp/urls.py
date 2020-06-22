from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('home/', views.home),
    path('engneering-colleges/', views.engneeringColleges),
    path('medical-colleges/', views.medicalColleges),
    path('diploma-colleges/', views.diplomaColleges),
    path('top-iit/', views.topIIT),
    path('top-engneering-colleges/', views.topEngneeringColleges),
    path('top-medical-colleges/', views.topMedicalColleges),
    path('top-diploma-colleges/', views.topDiplomaColleges),
    path('states/<int:state_id>/', views.state),
]