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
                                                           'isStateNotSelected': isStateNotSelected,
                                                           'bottomCardLists': getBottomCardsObjectList()})


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
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'allEngneeringCollegesList': allEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def iitColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allIITColleges = AllColleges.objects.filter(college_type='iit').order_by('-college_rank')
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'allIITCollegesList': allIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


def topIITColleges(request):
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topIITCollegesList = []
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topEngneeringColleges(request):
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topEngneeringCollegesList = []
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topEngneeringCollegesList': topEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topMedicalColleges(request):
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topMedicalCollegesList = []
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topDiplomaColleges(request):
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topDiplomaCollegesList = []
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allEngneeringCollegesList': allEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allEngneeringCollegesList': allEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allEngneeringCollegesList': allEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def iitCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allIITColleges = AllColleges.objects.filter(college_type='iit', state_name=state_id).order_by(
        '-college_rank')
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'allIITCollegesList': allIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def iitCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allIITColleges = AllColleges.objects.filter(college_type='iit', city_name=city_id).order_by(
        '-college_rank')
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'allIITCollegesList': allIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def iitCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allIITColleges = AllColleges.objects.filter(college_type='iit', city_name=city_id).order_by(
        '-college_rank')
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'allIITCollegesList': allIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allMedicalColleges': allMedicalColleges, 'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allMedicalColleges': allMedicalColleges, 'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allDiplomaColleges': allDiplomaColleges, 'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


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
                   'allDiplomaColleges': allDiplomaColleges, 'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList()})


def topEngneeringCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4,
                                                       state_name=state_id).order_by(
        '-college_rank')
    topEngneeringCollegesList = []
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'topEngneeringCollegesList': topEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topEngneeringCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4,
                                                       city_name=city_id).order_by(
        '-college_rank')
    topEngneeringCollegesList = []
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topEngneeringCollegesList': topEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topEngneeringCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4,
                                                       city_name=city_id).order_by(
        '-college_rank')
    topEngneeringCollegesList = []
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'topEngneeringCollegesList': topEngneeringCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topMedicalCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4,
                                                    state_name=state_id).order_by(
        '-college_rank')
    topMedicalCollegesList = []
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topMedicalCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4,
                                                    city_name=city_id).order_by(
        '-college_rank')
    topMedicalCollegesList = []
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topMedicalCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topEngneeringColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4,
                                                       city_name=city_id).order_by(
        '-college_rank')
    topMedicalCollegesList = []
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topDiplomaCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4,
                                                    state_name=state_id).order_by(
        '-college_rank')
    topDiplomaCollegesList = []
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topDiplomaCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4,
                                                    city_name=city_id).order_by(
        '-college_rank')
    topDiplomaCollegesList = []
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topDiplomaCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4,
                                                    city_name=city_id).order_by(
        '-college_rank')
    topDiplomaCollegesList = []
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topIITCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4, state_name=state_id).order_by(
        '-college_rank')
    topIITCollegesList = []
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topIITCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4, city_name=city_id).order_by(
        '-college_rank')
    topIITCollegesList = []
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topIITCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4, city_name=city_id).order_by(
        '-college_rank')
    topIITCollegesList = []
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList()})


def topGovernmentEngineeringColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='engneering',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Government Engineering Colleges in India'
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topColleges': topColleges, 'heading': heading
    })


def topPrivateEngineeringColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='engneering',
                                             college_status='private').order_by(
        '-college_rank')
    heading = 'Top Private Engineering Colleges in India'
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topColleges': topColleges, 'heading': heading
    })


def topGovernmentMedicalColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='medical',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Government Medical Colleges in India'
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topColleges': topColleges, 'heading': heading
    })


def topGovernmentDiplomaColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='diploma',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Government Diploma Colleges in India'
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topColleges': topColleges, 'heading': heading
    })


def topPrivateDiplomaColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='diploma',
                                             college_status='private').order_by('-college_rank')
    heading = 'Top Private Diploma Colleges in India'
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topColleges': topColleges, 'heading': heading
    })


def getBottomCardsObjectList():
    description = 'Get all top colleges name, their rank, semister fees, college official site link and manny more details.'
    card1 = MyBottomCard('Top Government Engineering Colleges in India', description,
                         '/top-government-engineering-colleges/', '/media/all_images/heritage.jpg', '#80c497')
    card2 = MyBottomCard('Top Private Engineering Colleges in India', description, '/top-private-engineering-colleges/',
                         '/media/all_images/heritage2.jpg', '#ba80c4')
    card3 = MyBottomCard('Top Government Medical Colleges in India', description, '/top-government-medical-colleges/',
                         '/media/all_images/hit_haldia3.jpg', '#46f252')
    card4 = MyBottomCard('Top Government Diploma Colleges in India', description, '/top-government-diploma-colleges/',
                         '/media/all_images/hit_haldia.jpg', '#e6aa73')
    card5 = MyBottomCard('Top Private Diploma Colleges in India', description, '/top-private-diploma-colleges/',
                         '/media/all_images/medical2_PeOtCx2.jpg', '#eb6ab7')
    bottomCardLists = [card1, card2, card3, card4, card5]
    return bottomCardLists
