from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def home(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/home.html', {'firstState': firstState, 'allCitiesList': allCitiesList,
                                                           'allStatesListForDropdown': allStatesListForDropdown,
                                                           'otherThreeStates': otherThreeStates,
                                                           'isStateNotSelected': isStateNotSelected})


def engneeringColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected})


def medicalColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected})


def diplomaColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected})


def topIIT(request):
    return HttpResponse("Top IIT")


def topEngneeringColleges(request):
    return HttpResponse("Top Engneering Colleges")


def topMedicalColleges(request):
    return HttpResponse("Top Medical Colleges")


def topDiplomaColleges(request):
    return HttpResponse("Top Diploma Colleges")


def homeCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/home.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state})


def homeCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/home.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id})


def homeCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/home.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state})


def engneeringCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state})


def engneeringCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id})


def engneeringCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state})


def medicalCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state})


def medicalCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id})


def medicalCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state})


def diplomaCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state})


def diplomaCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id})


def diplomaCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    state = "/state"
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state})
