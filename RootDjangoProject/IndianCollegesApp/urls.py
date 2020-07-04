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

    path('top-government-engineering-colleges/', views.topGovernmentEngineeringColleges),
    path('top-private-engineering-colleges/', views.topPrivateEngineeringColleges),
    path('top-government-medical-colleges/', views.topGovernmentMedicalColleges),
    path('top-government-diploma-colleges/', views.topGovernmentDiplomaColleges),
    path('top-private-diploma-colleges/', views.topPrivateDiplomaColleges),
    path('top-best-iit-colleges/', views.topBestIITColleges),

    path('engineering-colleges/college-type/<str:college_status>', views.engineeringCollegesFilterByCollegeType),
    path('engineering-colleges/state/<int:state_id>/college-type/<str:college_status>', views.engineeringCollegesStateWiseFilterByCollegeType),
    path('engineering-colleges/city/<int:city_id>/college-type/<str:college_status>', views.engineeringCollegesCityWiseFilterByCollegeType),
    path('engineering-colleges/state/city/<int:city_id>/college-type/<str:college_status>', views.engineeringCollegesStateCityWiseFilterByCollegeType),

    path('iit-colleges/college-type/<str:college_status>', views.iitCollegesFilterByCollegeType),
    path('iit-colleges/state/<int:state_id>/college-type/<str:college_status>',
         views.iitCollegesStateWiseFilterByCollegeType),
    path('iit-colleges/city/<int:city_id>/college-type/<str:college_status>',
         views.iitCollegesCityWiseFilterByCollegeType),
    path('iit-colleges/state/city/<int:city_id>/college-type/<str:college_status>',
         views.iitCollegesStateCityWiseFilterByCollegeType),


    path('medical-colleges/college-type/<str:college_status>', views.medicalCollegesFilterByCollegeType),
    path('medical-colleges/state/<int:state_id>/college-type/<str:college_status>',
         views.medicalCollegesStateWiseFilterByCollegeType),
    path('medical-colleges/city/<int:city_id>/college-type/<str:college_status>',
         views.medicalCollegesCityWiseFilterByCollegeType),
    path('medical-colleges/state/city/<int:city_id>/college-type/<str:college_status>',
         views.medicalCollegesStateCityWiseFilterByCollegeType),

    path('diploma-colleges/college-type/<str:college_status>', views.diplomaCollegesFilterByCollegeType),
    path('diploma-colleges/state/<int:state_id>/college-type/<str:college_status>',
         views.diplomaCollegesStateWiseFilterByCollegeType),
    path('diploma-colleges/city/<int:city_id>/college-type/<str:college_status>',
         views.diplomaCollegesCityWiseFilterByCollegeType),
    path('diploma-colleges/state/city/<int:city_id>/college-type/<str:college_status>',
         views.diplomaCollegesStateCityWiseFilterByCollegeType),

    path('top-iit-colleges/college-type/<str:college_status>', views.topIITCollegesFilterByCollegeType),
    path('top-iit-colleges/state/<int:state_id>/college-type/<str:college_status>',
         views.topIITCollegesStateWiseFilterByCollegeType),
    path('top-iit-colleges/city/<int:city_id>/college-type/<str:college_status>',
         views.topIITCollegesCityWiseFilterByCollegeType),
    path('top-iit-colleges/state/city/<int:city_id>/college-type/<str:college_status>',
         views.topIITCollegesStateCityWiseFilterByCollegeType),

    path('top-diploma-colleges/college-type/<str:college_status>', views.topDiplomaCollegesFilterByCollegeType),
    path('top-diploma-colleges/state/<int:state_id>/college-type/<str:college_status>',
         views.topDiplomaCollegesStateWiseFilterByCollegeType),
    path('top-diploma-colleges/city/<int:city_id>/college-type/<str:college_status>',
         views.topDiplomaCollegesCityWiseFilterByCollegeType),
    path('top-diploma-colleges/state/city/<int:city_id>/college-type/<str:college_status>',
         views.topDiplomaCollegesStateCityWiseFilterByCollegeType),

    path('top-medical-colleges/college-type/<str:college_status>', views.topMedicalCollegesFilterByCollegeType),
    path('top-medical-colleges/state/<int:state_id>/college-type/<str:college_status>',
         views.topMedicalCollegesStateWiseFilterByCollegeType),
    path('top-medical-colleges/city/<int:city_id>/college-type/<str:college_status>',
         views.topMedicalCollegesCityWiseFilterByCollegeType),
    path('top-medical-colleges/state/city/<int:city_id>/college-type/<str:college_status>',
         views.topMedicalCollegesStateCityWiseFilterByCollegeType),

    path('top-engineering-colleges/college-type/<str:college_status>', views.topEngineeringCollegesFilterByCollegeType),
    path('top-engineering-colleges/state/<int:state_id>/college-type/<str:college_status>',
         views.topEngineeringCollegesStateWiseFilterByCollegeType),
    path('top-engineering-colleges/city/<int:city_id>/college-type/<str:college_status>',
         views.topEngineeringCollegesCityWiseFilterByCollegeType),
    path('top-engineering-colleges/state/city/<int:city_id>/college-type/<str:college_status>',
         views.topEngineeringCollegesStateCityWiseFilterByCollegeType),


    path('engineering-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>', views.engineeringCollegesFilterBySemesterFees),
    path('engineering-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.engineeringCollegesStateWiseFilterBySemesterFees),
    path('engineering-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.engineeringCollegesCityWiseFilterBySemesterFees),
    path('engineering-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.engineeringCollegesStateCityWiseFilterBySemesterFees),

    path('iit-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.iitCollegesFilterBySemesterFees),
    path('iit-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.iitCollegesStateWiseFilterBySemesterFees),
    path('iit-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.iitCollegesCityWiseFilterBySemesterFees),
    path('iit-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.iitCollegesStateCityWiseFilterBySemesterFees),

    path('medical-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.medicalCollegesFilterBySemesterFees),
    path('medical-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.medicalCollegesStateWiseFilterBySemesterFees),
    path('medical-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.medicalCollegesCityWiseFilterBySemesterFees),
    path('medical-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.medicalCollegesStateCityWiseFilterBySemesterFees),

    path('diploma-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.diplomaCollegesFilterBySemesterFees),
    path('diploma-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.diplomaCollegesStateWiseFilterBySemesterFees),
    path('diploma-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.diplomaCollegesCityWiseFilterBySemesterFees),
    path('diploma-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.diplomaCollegesStateCityWiseFilterBySemesterFees),


    path('top-iit-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.topIITCollegesFilterBySemesterFees),
    path('top-iit-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topIITCollegesStateWiseFilterBySemesterFees),
    path('top-iit-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topIITCollegesCityWiseFilterBySemesterFees),
    path('top-iit-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topIITCollegesStateCityWiseFilterBySemesterFees),


    path('top-diploma-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.topDiplomaCollegesFilterBySemesterFees),
    path('top-diploma-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topDiplomaCollegesStateWiseFilterBySemesterFees),
    path('top-diploma-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topDiplomaCollegesCityWiseFilterBySemesterFees),
    path('top-diploma-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topDiplomaCollegesStateCityWiseFilterBySemesterFees),

    path('top-medical-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.topMedicalCollegesFilterBySemesterFees),
    path('top-medical-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topMedicalCollegesStateWiseFilterBySemesterFees),
    path('top-medical-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topMedicalCollegesCityWiseFilterBySemesterFees),
    path('top-medical-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topMedicalCollegesStateCityWiseFilterBySemesterFees),

    path('top-engineering-colleges/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
         views.topEngineeringCollegesFilterBySemesterFees),
    path('top-engineering-colleges/state/<int:state_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topEngineeringCollegesStateWiseFilterBySemesterFees),
    path('top-engineering-colleges/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topEngineeringCollegesCityWiseFilterBySemesterFees),
    path('top-engineering-colleges/state/city/<int:city_id>/semester-fees/<str:lower_value>/<str:higher_value>/<int:selected_link_number>',
        views.topEngineeringCollegesStateCityWiseFilterBySemesterFees),

]









