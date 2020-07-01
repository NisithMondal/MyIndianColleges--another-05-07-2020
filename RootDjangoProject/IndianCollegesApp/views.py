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
    bodyTitle = 'College data not Available'
    if len(allEngneeringColleges) > 0:
        bodyTitle = 'All Engineering Colleges in India'
    allEngneeringCollegesList = []
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'allEngneeringCollegesList': allEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def iitColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allIITColleges = AllColleges.objects.filter(college_type='iit').order_by('-college_rank')
    bodyTitle = 'College data not Available'
    if len(allIITColleges) > 0:
        bodyTitle = 'All IIT Colleges in India'
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'allIITCollegesList': allIITCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def medicalColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allMedicalColleges = AllColleges.objects.filter(college_type='medical').order_by('-college_rank')
    bodyTitle = 'College data not Available'
    if len(allMedicalColleges) > 0:
        bodyTitle = 'All Medical Colleges in India'
    allImages = CollegeImages.objects.get(id=3)
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'allMedicalColleges': allMedicalColleges,
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def diplomaColleges(request):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allDiplomaColleges = AllColleges.objects.filter(college_type='diploma').order_by('-college_rank')
    bodyTitle = 'College data not Available'
    if len(allDiplomaColleges) > 0:
        bodyTitle = 'All Diploma Colleges in India'
    allImages = CollegeImages.objects.get(id=1)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'allDiplomaColleges': allDiplomaColleges,
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topIITColleges(request):
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    bodyTitle = 'College data not Available'
    if len(topIITColleges) > 0:
        bodyTitle = 'Top IIT Colleges in India'
    topIITCollegesList = []
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topEngneeringColleges(request):
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    bodyTitle = 'College data not Available'
    if len(topEngneeringColleges) > 0:
        bodyTitle = 'Top Engineering Colleges in India'
    topEngneeringCollegesList = []
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topEngneeringCollegesList': topEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topMedicalColleges(request):
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    bodyTitle = 'College data not Available'
    if len(topMedicalColleges) > 0:
        bodyTitle = 'Top Medical Colleges in India'
    topMedicalCollegesList = []
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topDiplomaColleges(request):
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4).order_by(
        '-college_rank')
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    bodyTitle = 'College data not Available'
    if len(topDiplomaColleges) > 0:
        bodyTitle = 'Top Diploma Colleges in India'
    topDiplomaCollegesList = []
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


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
    bodyTitle = 'College data is not Available of this State '
    if len(allEngneeringColleges) > 0:
        bodyTitle = 'Engineering Colleges in '+selectedState.state_name
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
                   'allEngneeringCollegesList': allEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def engneeringCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allEngneeringColleges = AllColleges.objects.filter(college_type='engneering', city_name=city_id).order_by(
        '-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(allEngneeringColleges) > 0:
        bodyTitle = 'Engineering Colleges in ' + selectedCity.city_name + ', ' +str(selectedCity.state_id)
    allEngneeringCollegesList = []
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'allEngneeringCollegesList': allEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def engneeringCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allEngneeringColleges = AllColleges.objects.filter(college_type='engneering', city_name=city_id).order_by(
        '-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(allEngneeringColleges) > 0:
        bodyTitle = 'Engineering Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
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
                   'allEngneeringCollegesList': allEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


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
    bodyTitle = 'College data is not Available of this State '
    if len(allIITColleges) > 0:
        bodyTitle = 'IIT Colleges in ' + selectedState.state_name
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'allIITCollegesList': allIITCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def iitCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allIITColleges = AllColleges.objects.filter(college_type='iit', city_name=city_id).order_by(
        '-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(allIITColleges) > 0:
        bodyTitle = 'Engineering Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'allIITCollegesList': allIITCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def iitCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allIITColleges = AllColleges.objects.filter(college_type='iit', city_name=city_id).order_by(
        '-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(allIITColleges) > 0:
        bodyTitle = 'IIT Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
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
                   'allIITCollegesList': allIITCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


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
    bodyTitle = 'College data is not Available of this State '
    if len(allMedicalColleges) > 0:
        bodyTitle = 'Medical Colleges in ' + selectedState.state_name
    allImages = CollegeImages.objects.get(id=6)
    state = "/state"
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'allMedicalColleges': allMedicalColleges,
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def medicalCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allMedicalColleges = AllColleges.objects.filter(college_type='medical', city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(allMedicalColleges) > 0:
        bodyTitle = 'Medical Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    allImages = CollegeImages.objects.get(id=7)
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'allMedicalColleges': allMedicalColleges, 'allImages': allImages,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def medicalCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allMedicalColleges = AllColleges.objects.filter(college_type='medical', city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(allMedicalColleges) > 0:
        bodyTitle = 'Medical Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
    allImages = CollegeImages.objects.get(id=7)
    state = "/state"
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'allMedicalColleges': allMedicalColleges, 'allImages': allImages,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


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
    bodyTitle = 'College data is not Available of this State '
    if len(allDiplomaColleges) > 0:
        bodyTitle = 'Diploma Colleges in ' + selectedState.state_name
    allImages = CollegeImages.objects.get(id=3)
    state = "/state"
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'allDiplomaColleges': allDiplomaColleges,
                   'allImages': allImages, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def diplomaCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    allDiplomaColleges = AllColleges.objects.filter(college_type='diploma', city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(allDiplomaColleges) > 0:
        bodyTitle = 'Diploma Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    allImages = CollegeImages.objects.get(id=3)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'allDiplomaColleges': allDiplomaColleges, 'allImages': allImages,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def diplomaCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    allDiplomaColleges = AllColleges.objects.filter(college_type='diploma', city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(allDiplomaColleges) > 0:
        bodyTitle = 'Diploma Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
    allImages = CollegeImages.objects.get(id=3)
    state = "/state"
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'allDiplomaColleges': allDiplomaColleges, 'allImages': allImages,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topEngneeringCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4,
                                                       state_name=state_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this State '
    if len(topEngneeringColleges) > 0:
        bodyTitle = 'Top Engineering Colleges in ' + selectedState.state_name
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
                   'topEngneeringCollegesList': topEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topEngneeringCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4,
                                                       city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(topEngneeringColleges) > 0:
        bodyTitle = 'Top Engineering Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    topEngneeringCollegesList = []
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topEngneeringCollegesList': topEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topEngneeringCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topEngneeringColleges = AllColleges.objects.filter(college_type='engneering', college_rank__gte=4,
                                                       city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(topEngneeringColleges) > 0:
        bodyTitle = 'Top Engineering Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
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
                   'topEngneeringCollegesList': topEngneeringCollegesList,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topMedicalCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4, state_name=state_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this State '
    if len(topMedicalColleges) > 0:
        bodyTitle = 'Top Medical Colleges in ' + selectedState.state_name
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
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topMedicalCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4,
                                                    city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(topMedicalColleges) > 0:
        bodyTitle = 'Top Medical Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    topMedicalCollegesList = []
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topMedicalCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4,
                                                       city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(topMedicalColleges) > 0:
        bodyTitle = 'Top Medical Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
    topMedicalCollegesList = []
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    state = "/state"
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'topMedicalCollegesList': topMedicalCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topDiplomaCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4,
                                                    state_name=state_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this State '
    if len(topDiplomaColleges) > 0:
        bodyTitle = 'Top Diploma Colleges in ' + selectedState.state_name
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
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topDiplomaCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4,
                                                    city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(topDiplomaColleges) > 0:
        bodyTitle = 'Top Diploma Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    topDiplomaCollegesList = []
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topDiplomaCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topDiplomaColleges = AllColleges.objects.filter(college_type='diploma', college_rank__gte=4,
                                                    city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(topDiplomaColleges) > 0:
        bodyTitle = 'Top Diploma Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
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
                   'topDiplomaCollegesList': topDiplomaCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


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
    bodyTitle = 'College data is not Available of this State '
    if len(topIITColleges) > 0:
        bodyTitle = 'Top IIT Colleges in ' + selectedState.state_name
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
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topIITCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4, city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(topIITColleges) > 0:
        bodyTitle = 'Top IIT Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    topIITCollegesList = []
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


def topIITCollegesStateCityWise(request, city_id):
    obj = AllCities.objects.get(id=city_id)
    state_id = obj.state_id_id
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    selectedCity = AllCities.objects.get(id=city_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4, city_name=city_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(topIITColleges) > 0:
        bodyTitle = 'Top IIT Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
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
                   'topIITCollegesList': topIITCollegesList, 'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle})


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


def topBestIITColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='iit',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Best IIT Colleges in India'
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
    card6 = MyBottomCard('Top Best IIT Colleges in India', description, '/top-best-iit-colleges/',
                         '/media/all_images/mycollege.jpg', '#70d4b9')
    bottomCardLists = [card1, card2, card3, card4, card5, card6]
    return bottomCardLists
