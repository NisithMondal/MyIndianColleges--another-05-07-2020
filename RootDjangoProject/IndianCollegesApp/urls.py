from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('home/', views.home),
    path('engneering-colleges/', views.engneeringColleges),
    path('iit-colleges/', views.iitColleges),
    path('medical-colleges/', views.medicalColleges),
    path('diploma-colleges/', views.diplomaColleges),

    path('top-iit/', views.topIITColleges),
    path('top-engneering-colleges/', views.topEngneeringColleges),
    path('top-medical-colleges/', views.topMedicalColleges),
    path('top-diploma-colleges/', views.topDiplomaColleges),

    path('home/states/<int:state_id>/', views.homeCollegesStateWise),
    path('home/city/<int:city_id>/', views.homeCollegesCityWise),
    path('home/state/city/<int:city_id>/', views.homeCollegesStateCityWise),

    path('engneering-colleges/states/<int:state_id>/', views.engneeringCollegesStateWise),
    path('engneering-colleges/city/<int:city_id>/', views.engneeringCollegesCityWise),
    path('engneering-colleges/state/city/<int:city_id>/', views.engneeringCollegesStateCityWise),

    path('iit-colleges/states/<int:state_id>/', views.iitCollegesStateWise),
    path('iit-colleges/city/<int:city_id>/', views.iitCollegesCityWise),
    path('iit-colleges/state/city/<int:city_id>/', views.iitCollegesStateCityWise),

    path('medical-colleges/states/<int:state_id>/', views.medicalCollegesStateWise),
    path('medical-colleges/city/<int:city_id>/', views.medicalCollegesCityWise),
    path('medical-colleges/state/city/<int:city_id>/', views.medicalCollegesStateCityWise),

    path('diploma-colleges/states/<int:state_id>/', views.diplomaCollegesStateWise),
    path('diploma-colleges/city/<int:city_id>/', views.diplomaCollegesCityWise),
    path('diploma-colleges/state/city/<int:city_id>/', views.diplomaCollegesStateCityWise),

    path('top-engneering-colleges/states/<int:state_id>/', views.topEngneeringCollegesStateWise),
    path('top-engneering-colleges/city/<int:city_id>/', views.topEngneeringCollegesCityWise),
    path('top-engneering-colleges/state/city/<int:city_id>/', views.topEngneeringCollegesStateCityWise),

    path('top-medical-colleges/states/<int:state_id>/', views.topMedicalCollegesStateWise),
    path('top-medical-colleges/city/<int:city_id>/', views.topMedicalCollegesCityWise),
    path('top-medical-colleges/state/city/<int:city_id>/', views.topMedicalCollegesStateCityWise),

    path('top-diploma-colleges/states/<int:state_id>/', views.topDiplomaCollegesStateWise),
    path('top-diploma-colleges/city/<int:city_id>/', views.topDiplomaCollegesCityWise),
    path('top-diploma-colleges/state/city/<int:city_id>/', views.topDiplomaCollegesStateCityWise),

    path('top-iit-colleges/states/<int:state_id>/', views.topIITCollegesStateWise),
    path('top-iit-colleges/city/<int:city_id>/', views.topIITCollegesCityWise),
    path('top-iit-colleges/state/city/<int:city_id>/', views.topIITCollegesStateCityWise),




]