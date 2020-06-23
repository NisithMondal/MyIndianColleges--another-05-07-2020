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

    path('home/states/<int:state_id>/', views.homeCollegesStateWise),
    path('home/city/<int:city_id>/', views.homeCollegesCityWise),
    path('home/state/city/<int:city_id>/', views.homeCollegesStateCityWise),


    path('engneering-colleges/states/<int:state_id>/', views.engneeringCollegesStateWise),
    path('engneering-colleges/city/<int:city_id>/', views.engneeringCollegesCityWise),
    path('engneering-colleges/state/city/<int:city_id>/', views.engneeringCollegesStateCityWise),

    path('medical-colleges/states/<int:state_id>/', views.medicalCollegesStateWise),
    path('medical-colleges/city/<int:city_id>/', views.medicalCollegesCityWise),
    path('medical-colleges/state/city/<int:city_id>/', views.medicalCollegesStateCityWise),

    path('diploma-colleges/states/<int:state_id>/', views.diplomaCollegesStateWise),
    path('diploma-colleges/city/<int:city_id>/', views.diplomaCollegesCityWise),
    path('diploma-colleges/state/city/<int:city_id>/', views.diplomaCollegesStateCityWise),

]