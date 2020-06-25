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
    allEngneeringColleges = AllColleges.objects.filter(college_type='engneering').order_by('-college_rank')
    allEngneeringCollegesList = []
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'allEngneeringCollegesList': allEngneeringCollegesList})


def medicalColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allMedicalColleges = AllColleges.objects.filter(college_type='medical').order_by('-college_rank')
    allImages = CollegeImages.objects.get(id=3)
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'allMedicalColleges': allMedicalColleges,
                   'allImages': allImages})


def diplomaColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allDiplomaColleges = AllColleges.objects.filter(college_type='diploma').order_by('-college_rank')
    allImages = CollegeImages.objects.get(id=1)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'allDiplomaColleges': allDiplomaColleges,
                   'allImages': allImages})


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
    allEngneeringColleges = AllColleges.objects.filter(college_type='engneering', state_name=state_id).order_by(
        '-college_rank')
    allEngneeringCollegesList = []
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'allEngneeringCollegesList': allEngneeringCollegesList})


def engneeringCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allEngneeringColleges = AllColleges.objects.filter(college_type='engneering', city_name=city_id).order_by(
        '-college_rank')
    allEngneeringCollegesList = []
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                      {'firstState': firstState, 'allCitiesList': allCitiesList,
                       'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                       'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                       'allEngneeringCollegesList': allEngneeringCollegesList})


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
    allEngneeringColleges = AllColleges.objects.filter(college_type='engneering', city_name=city_id).order_by(
        '-college_rank')
    allEngneeringCollegesList = []
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'allEngneeringCollegesList': allEngneeringCollegesList})


def medicalCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allMedicalColleges = AllColleges.objects.filter(college_type='medical', state_name=state_id).order_by(
        '-college_rank')
    allImages = CollegeImages.objects.get(id=6)
    state = "/state"
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'allMedicalColleges': allMedicalColleges,
                   'allImages': allImages})


def medicalCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allMedicalColleges = AllColleges.objects.filter(college_type='medical', city_name=city_id).order_by('-college_rank')
    allImages = CollegeImages.objects.get(id=7)
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'allMedicalColleges': allMedicalColleges, 'allImages': allImages})


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
    allMedicalColleges = AllColleges.objects.filter(college_type='medical', city_name=city_id).order_by('-college_rank')
    allImages = CollegeImages.objects.get(id=7)
    state = "/state"
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'allMedicalColleges': allMedicalColleges, 'allImages': allImages})


def diplomaCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allDiplomaColleges = AllColleges.objects.filter(college_type='diploma', state_name=state_id).order_by(
        '-college_rank')
    allImages = CollegeImages.objects.get(id=3)
    state = "/state"
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'allDiplomaColleges': allDiplomaColleges,
                   'allImages': allImages})


def diplomaCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allDiplomaColleges = AllColleges.objects.filter(college_type='diploma', city_name=city_id).order_by('-college_rank')
    allImages = CollegeImages.objects.get(id=3)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'allDiplomaColleges': allDiplomaColleges, 'allImages': allImages})


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
    allDiplomaColleges = AllColleges.objects.filter(college_type='diploma', city_name=city_id).order_by('-college_rank')
    allImages = CollegeImages.objects.get(id=3)
    state = "/state"
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'allDiplomaColleges': allDiplomaColleges, 'allImages': allImages})
