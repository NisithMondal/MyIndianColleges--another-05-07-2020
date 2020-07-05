from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *


number_of_items_in_page = 3

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
    isListEmpty = False
    if len(allEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
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
    isListEmpty = False
    if len(allIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty})


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
    allMedicalCollegesList = []
    for college in allMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allMedicalCollegesList.append(college)
    isListEmpty = False
    if len(allMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)

    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'pageObj': page_obj,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty})


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
    allDiplomaCollegesList = []
    for college in allDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allDiplomaCollegesList.append(college)
    isListEmpty = False
    if len(allDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'pageObj': page_obj,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty})


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
    isListEmpty = False
    if len(topIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty})


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
    isListEmpty = False
    if len(topEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
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
    isListEmpty = False
    if len(topMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty})


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
    isListEmpty = False
    if len(topDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty})


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
        bodyTitle = 'Engineering Colleges in ' + selectedState.state_name
    allEngneeringCollegesList = []
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
        bodyTitle = 'Engineering Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    allEngneeringCollegesList = []
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    isListEmpty = False
    if len(allEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    for college in allEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allEngneeringCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'pageObj': page_obj,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    allIITCollegesList = []
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    isListEmpty = False
    if len(allIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'isListEmpty': isListEmpty,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    for college in allIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allIITCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue,
                   'collegeFeesUrlValue': collegeFeesUrlValue, 'isListEmpty': isListEmpty})


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
    allMedicalCollegesList = []
    for college in allMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allMedicalCollegesList.append(college)
    state = "/state"
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    isListEmpty = False
    if len(allMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'pageObj': page_obj,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue, 'isListEmpty': isListEmpty})


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
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    if len(allMedicalColleges) > 0:
        bodyTitle = 'Medical Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    allMedicalCollegesList = []
    for college in allMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allMedicalCollegesList.append(college)
    isListEmpty = False
    if len(allMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'pageObj': page_obj,'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    if len(allMedicalColleges) > 0:
        bodyTitle = 'Medical Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
    allMedicalCollegesList = []
    for college in allMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allMedicalCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj,'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    allDiplomaCollegesList = []
    for college in allDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allDiplomaCollegesList.append(college)
    state = "/state"
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    isListEmpty = False
    if len(allDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'pageObj': page_obj,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle, 'isListEmpty': isListEmpty,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    if len(allDiplomaColleges) > 0:
        bodyTitle = 'Diploma Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    allDiplomaCollegesList = []
    for college in allDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allDiplomaCollegesList.append(college)
    isListEmpty = False
    if len(allDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    if len(allDiplomaColleges) > 0:
        bodyTitle = 'Diploma Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
    allDiplomaCollegesList = []
    for college in allDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allDiplomaCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    isListEmpty = False
    if len(topEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    for college in topEngneeringColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topEngneeringCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topEngneeringCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topEngneeringCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_engneering_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


def topMedicalCollegesStateWise(request, state_id):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    topMedicalColleges = AllColleges.objects.filter(college_type='medical', college_rank__gte=4,
                                                    state_name=state_id).order_by('-college_rank')
    bodyTitle = 'College data is not Available of this State '
    if len(topMedicalColleges) > 0:
        bodyTitle = 'Top Medical Colleges in ' + selectedState.state_name
    topMedicalCollegesList = []
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'isListEmpty': isListEmpty,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    isListEmpty = False
    if len(topMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'isListEmpty': isListEmpty,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    for college in topMedicalColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topMedicalCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topMedicalCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topMedicalCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_medical_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue,
                   'collegeFeesUrlValue': collegeFeesUrlValue, 'isListEmpty': isListEmpty})


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
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'isListEmpty': isListEmpty,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    isListEmpty = False
    if len(topDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'isListEmpty': isListEmpty,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    for college in topDiplomaColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topDiplomaCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topDiplomaCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topDiplomaCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_diploma_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue,
                   'collegeFeesUrlValue': collegeFeesUrlValue, 'isListEmpty': isListEmpty})


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
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state, 'isListEmpty': isListEmpty,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


def topIITCollegesCityWise(request, city_id):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4, city_name=city_id).order_by(
        '-college_rank')
    bodyTitle = 'College data is not Available ot this City '
    if len(topIITColleges) > 0:
        bodyTitle = 'Top IIT Colleges in ' + selectedCity.city_name + ', ' + str(selectedCity.state_id)
    topIITCollegesList = []
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    isListEmpty = False
    if len(topIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'isListEmpty': isListEmpty,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(),
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


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
    topIITColleges = AllColleges.objects.filter(college_type='iit', college_rank__gte=4, city_name=city_id).order_by(
        '-college_rank')
    bodyTitle = 'College data is not Available of this City'
    if len(topIITColleges) > 0:
        bodyTitle = 'Top IIT Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
    topIITCollegesList = []
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    for college in topIITColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topIITCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(topIITCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(topIITCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/top_iit_colleges.html',
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'bottomCardLists': getBottomCardsObjectList(), 'isListEmpty': isListEmpty,
                   'bodyTitle': bodyTitle, 'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue})


def topGovernmentEngineeringColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='engneering',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Government Engineering Colleges in India'
    topCollegesList = []
    for college in topColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topCollegesList.append(college)
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topCollegesList': topCollegesList, 'heading': heading
    })


def topPrivateEngineeringColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='engneering',
                                             college_status='private').order_by(
        '-college_rank')
    heading = 'Top Private Engineering Colleges in India'
    topCollegesList = []
    for college in topColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topCollegesList.append(college)
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topCollegesList': topCollegesList, 'heading': heading
    })


def topGovernmentMedicalColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='medical',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Government Medical Colleges in India'
    topCollegesList = []
    for college in topColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topCollegesList.append(college)
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topCollegesList': topCollegesList, 'heading': heading
    })


def topGovernmentDiplomaColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='diploma',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Government Diploma Colleges in India'
    topCollegesList = []
    for college in topColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topCollegesList.append(college)
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topCollegesList': topCollegesList, 'heading': heading
    })


def topPrivateDiplomaColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='diploma',
                                             college_status='private').order_by('-college_rank')
    heading = 'Top Private Diploma Colleges in India'
    topCollegesList = []
    for college in topColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topCollegesList.append(college)
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topCollegesList': topCollegesList, 'heading': heading
    })


def topBestIITColleges(request):
    topColleges = AllColleges.objects.filter(college_rank__gte=4, college_type='iit',
                                             college_status='government').order_by('-college_rank')
    heading = 'Top Best IIT Colleges in India'
    topCollegesList = []
    for college in topColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        topCollegesList.append(college)
    return render(request, 'IndianCollegesApp/bottom_cards_college_page.html', {
        'topCollegesList': topCollegesList, 'heading': heading
    })


def engineeringCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'engneering', 'engneering_colleges.html', False)


def iitCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'iit', 'iit_colleges.html', False)


def medicalCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'medical', 'medical_colleges.html', False)


def diplomaCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'diploma', 'diploma_colleges.html', False)


def topIITCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'iit', 'top_iit_colleges.html', True)


def topDiplomaCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'diploma', 'top_diploma_colleges.html', True)


def topMedicalCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'medical', 'top_medical_colleges.html', True)


def topEngineeringCollegesFilterByCollegeType(request, college_status):
    return filterByCollegeType(request, college_status, 'engneering', 'top_engneering_colleges.html', True)


def filterByCollegeType(request, college_status, college_type, template_name, isRequestForTopColleges):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    if isRequestForTopColleges:
        allColleges = AllColleges.objects.filter(college_type=college_type,
                                                 college_status=college_status, college_rank__gte=4).order_by(
            '-college_rank')
    else:
        allColleges = AllColleges.objects.filter(college_type=college_type,
                                                 college_status=college_status).order_by('-college_rank')
    bodyTitle = 'Colleges not Found'
    if len(allColleges) > 0:
        bodyTitle = 'All ' + str.capitalize(college_status) + ' ' + str.capitalize(college_type) + ' Colleges in India'
    allCollegesList = []
    # for type government selected link value = 1
    selectedLink = 1
    if college_status == 'private':
        selectedLink = 2
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + template_name,
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle, 'selectedLink': selectedLink})


def engineeringCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'engneering', 'engneering_colleges.html', False)


def iitCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'iit', 'iit_colleges.html', False)


def medicalCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'medical', 'medical_colleges.html', False)


def diplomaCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'diploma', 'diploma_colleges.html', False)


def topIITCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'iit', 'top_iit_colleges.html', True)


def topDiplomaCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'diploma', 'top_diploma_colleges.html', True)


def topMedicalCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'medical', 'top_medical_colleges.html', True)


def topEngineeringCollegesStateWiseFilterByCollegeType(request, state_id, college_status):
    return StateWiseFilterByCollegeType(request, state_id, college_status, 'engneering', 'top_engneering_colleges.html', True)


def StateWiseFilterByCollegeType(request, state_id, college_status, college_type, templet_name, isRequestForTopColleges):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    if isRequestForTopColleges:
        allColleges = AllColleges.objects.filter(college_type=college_type, college_status=college_status,
                                                 state_name=state_id, college_rank__gte=4).order_by('-college_rank')
    else:
        allColleges = AllColleges.objects.filter(college_type=college_type, college_status=college_status,
                                                 state_name=state_id).order_by('-college_rank')
    bodyTitle = str.capitalize(college_status) + ' College is not Found of this State '
    if len(allColleges) > 0:
        bodyTitle = str.capitalize(college_status) + ' ' + str.capitalize(
            college_type) + ' Colleges in ' + selectedState.state_name
    allCollegesList = []
    # for type government selected link value = 1
    selectedLink = 1
    if college_status == 'private':
        selectedLink = 2
    collegeTypeUrlValue = "/state/" + str(state_id)
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + templet_name,
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'selectedLink': selectedLink})


def engineeringCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'engneering', 'engneering_colleges.html', False)


def iitCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'iit', 'iit_colleges.html', False)


def medicalCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'medical', 'medical_colleges.html', False)


def diplomaCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'diploma', 'diploma_colleges.html', False)


def topIITCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'iit', 'top_iit_colleges.html', True)


def topDiplomaCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'diploma', 'top_diploma_colleges.html', True)


def topMedicalCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'medical', 'top_medical_colleges.html', True)


def topEngineeringCollegesCityWiseFilterByCollegeType(request, city_id, college_status):
    return cityWiseFilterByCollegeType(request, city_id, college_status, 'engneering', 'top_engneering_colleges.html', True)


def cityWiseFilterByCollegeType(request, city_id, college_status, college_type, templet_name, isRequestForTopColleges):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    if isRequestForTopColleges:
        allColleges = AllColleges.objects.filter(college_type=college_type, college_status=college_status,
                                                 city_name=city_id, college_rank__gte=4).order_by('-college_rank')
    else:
        allColleges = AllColleges.objects.filter(college_type=college_type, college_status=college_status,
                                                 city_name=city_id).order_by('-college_rank')
    bodyTitle = str.capitalize(college_status) + ' College is not Found of this City '
    if len(allColleges) > 0:
        bodyTitle = str.capitalize(college_status) + ' ' + str.capitalize(
            college_type) + ' Colleges in ' + selectedCity.city_name + ', ' + str(
            selectedCity.state_id)
    allCollegesList = []
    # for type government selected link value = 1
    selectedLink = 1
    if college_status == 'private':
        selectedLink = 2
    collegeTypeUrlValue = "/city/" + str(city_id)
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + templet_name,
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle, 'selectedLink': selectedLink,
                   'collegeTypeUrlValue': collegeTypeUrlValue})


def engineeringCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'engneering', 'engneering_colleges.html',
                                             False)


def iitCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'iit', 'iit_colleges.html',
                                             False)


def medicalCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'medical', 'medical_colleges.html',
                                             False)


def diplomaCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'diploma', 'diploma_colleges.html',
                                             False)


def topIITCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'iit', 'top_iit_colleges.html',
                                             True)


def topDiplomaCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'diploma', 'top_diploma_colleges.html',
                                             True)


def topMedicalCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'medical', 'top_medical_colleges.html',
                                             True)


def topEngineeringCollegesStateCityWiseFilterByCollegeType(request, city_id, college_status):
    return stateCityWiseFilterByCollegeType(request, city_id, college_status, 'engneering',
                                            'top_engneering_colleges.html',
                                             True)


def stateCityWiseFilterByCollegeType(request, city_id, college_status, college_type, template_name,
                                     isRequestForTopColleges):
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
    if isRequestForTopColleges:
        allColleges = AllColleges.objects.filter(college_type=college_type, college_status=college_status,
                                                 city_name=city_id, college_rank__gte=4).order_by('-college_rank')
    else:
        allColleges = AllColleges.objects.filter(college_type=college_type, college_status=college_status,
                                                 city_name=city_id).order_by('-college_rank')
    bodyTitle = str.capitalize(college_status) + ' College is not Found of this City'
    if len(allColleges) > 0:
        bodyTitle = str.capitalize(college_status) + ' ' + str.capitalize(
            college_type) + ' Colleges in ' + selectedCity.city_name + ', ' + selectedState.state_name
    allCollegesList = []
    # for type government selected link value = 1
    selectedLink = 1
    if college_status == 'private':
        selectedLink = 2
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + template_name,
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'selectedLink': selectedLink})


def engineeringCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'engneering',
                                'engneering_colleges.html', False)

def iitCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'iit',
                                'iit_colleges.html', False)

def medicalCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'medical',
                                'medical_colleges.html', False)


def diplomaCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'diploma',
                                'diploma_colleges.html', False)

def topIITCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'iit',
                                'top_iit_colleges.html', True)

def topDiplomaCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'diploma',
                                'top_diploma_colleges.html', True)


def topMedicalCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'medical',
                                'top_medical_colleges.html', True)


def topEngineeringCollegesFilterBySemesterFees(request, lower_value, higher_value, selected_link_number):
    return filterBySemesterFees(request, lower_value, higher_value, selected_link_number, 'engneering',
                                'top_engneering_colleges.html', True)



def filterBySemesterFees(request, lower_value, higher_value, selected_link_number, college_type, template_name,
                          isRequestForTopColleges):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    if isRequestForTopColleges:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')

    else:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')

    bodyTitle = 'College not Found in this Fees Range'
    if len(allColleges) > 0:
        bodyTitle = str.capitalize(
            college_type) + ' Colleges Semester Fees in between ' + lower_value + ' to ' + higher_value
    allCollegesList = []
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + template_name,
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown,
                   'otherThreeStates': otherThreeStates, 'isStateNotSelected': isStateNotSelected,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'feesSelectedLink': selected_link_number})


def engineeringCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'engneering',
                                         'engneering_colleges.html', False)


def iitCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'iit',
                                         'iit_colleges.html', False)


def medicalCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'medical',
                                         'medical_colleges.html', False)


def diplomaCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'diploma',
                                         'diploma_colleges.html', False)

def topIITCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'iit',
                                         'top_iit_colleges.html', True)

def topDiplomaCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'diploma',
                                         'top_diploma_colleges.html', True)


def topMedicalCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'medical',
                                         'top_medical_colleges.html', True)



def topEngineeringCollegesStateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value,
                                                     selected_link_number):
    return stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number,
                                         'engneering',
                                         'top_engneering_colleges.html', True)




def stateWiseFilterBySemesterFees(request, state_id, lower_value, higher_value, selected_link_number, college_type,
                                  template_name, isRequestForTopColleges):
    allStatesListForDropdown = list(AllStates.objects.exclude(id=state_id))
    selectedState = AllStates.objects.filter(id=state_id)
    allCitiesList = list(AllCities.objects.filter(state_id=state_id))
    selectedState = selectedState[0]
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = False
    if isRequestForTopColleges:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     state_name=state_id,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     state_name=state_id,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     state_name=state_id,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')

    else:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type, state_name=state_id,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type, state_name=state_id,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type, state_name=state_id,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')
    bodyTitle = 'College is not Found of this State in this Fees Range'
    if len(allColleges) > 0:
        bodyTitle = str.capitalize(
            college_type) + ' Colleges Semester Fees in between ' + lower_value + ' to ' + higher_value + ' in ' + selectedState.state_name
    allCollegesList = []
    collegeTypeUrlValue = "/state/" + str(state_id)
    collegeFeesUrlValue = "/state/" + str(state_id)
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + template_name,
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue,
                   'feesSelectedLink': selected_link_number})


def engineeringCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'engneering',
                                        'engneering_colleges.html', False)

def iitCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'iit',
                                        'iit_colleges.html', False)


def medicalCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'medical',
                                        'medical_colleges.html', False)


def diplomaCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'diploma',
                                        'diploma_colleges.html', False)


def topIITCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'iit',
                                        'top_iit_colleges.html', True)

def topDiplomaCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'diploma',
                                        'top_diploma_colleges.html', True)


def topMedicalCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'medical',
                                        'top_medical_colleges.html', True)


def topEngineeringCollegesCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number):
    return cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, 'engneering',
                                        'top_engneering_colleges.html', True)




def cityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, college_type,
                                 template_name, isRequestForTopColleges):
    allStatesListForDropdown = list(AllStates.objects.all())
    allCitiesList = list(AllCities.objects.all())
    selectedCity = AllCities.objects.get(id=city_id)
    firstState = allStatesListForDropdown.pop(0)
    otherThreeStates = [allStatesListForDropdown.pop(0), allStatesListForDropdown.pop(0),
                        allStatesListForDropdown.pop(0)]
    isStateNotSelected = True
    if isRequestForTopColleges:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     city_name=city_id,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     city_name=city_id,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     city_name=city_id,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')

    else:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type, city_name=city_id,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type, city_name=city_id,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type, city_name=city_id,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')

    bodyTitle = 'College is not Found of this City in this Fees Range'
    if len(allColleges) > 0:
        bodyTitle = str.capitalize(
            college_type) + ' Colleges Semester Fees in between ' + lower_value + ' to ' + higher_value + ' in ' + selectedCity.city_name + ', ' + str(
            selectedCity.state_id)
    allCollegesList = []
    collegeTypeUrlValue = "/city/" + str(city_id)
    collegeFeesUrlValue = "/city/" + str(city_id)
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + template_name,
                  {'firstState': firstState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'collegeFeesUrlValue': collegeFeesUrlValue,
                   'feesSelectedLink': selected_link_number})


def engineeringCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'engneering',
                                             'engneering_colleges.html', False)


def iitCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'iit',
                                             'iit_colleges.html', False)


def medicalCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'medical',
                                             'medical_colleges.html', 'allMedicalCollegesList', False)

def diplomaCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'diploma',
                                             'diploma_colleges.html', False)


def topIITCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'iit',
                                             'top_iit_colleges.html', True)


def topDiplomaCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'diploma',
                                             'top_diploma_colleges.html', True)


def topMedicalCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'medical',
                                             'top_medical_colleges.html', True)


def topEngineeringCollegesStateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value,
                                                         selected_link_number):
    return stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number,
                                             'engneering', 'top_engneering_colleges.html', True)


def stateCityWiseFilterBySemesterFees(request, city_id, lower_value, higher_value, selected_link_number, college_type,
                                      template_name, isRequestForTopColleges):
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
    if isRequestForTopColleges:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     city_name=city_id,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     city_name=city_id,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type, college_rank__gte=4,
                                                     city_name=city_id,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')

    else:
        if higher_value == 'greater':
            allColleges = AllColleges.objects.filter(college_type=college_type, city_name=city_id,
                                                     college_fees_per_semester__gt=lower_value).order_by(
                '-college_rank')

        elif higher_value == 'less':
            allColleges = AllColleges.objects.filter(college_type=college_type, city_name=city_id,
                                                     college_fees_per_semester__lte=lower_value).order_by(
                '-college_rank')

        else:
            allColleges = AllColleges.objects.filter(college_type=college_type, city_name=city_id,
                                                     college_fees_per_semester__gte=lower_value,
                                                     college_fees_per_semester__lte=higher_value).order_by(
                '-college_rank')
    bodyTitle = 'College is not Found of this City in this Fees Range'
    if len(allColleges) > 0:
        bodyTitle = str.capitalize(
            college_type) + ' Colleges Semester Fees in between ' + lower_value + ' to ' + higher_value + ' in ' + selectedCity.city_name + ', ' + str(
            selectedCity.state_id)
    allCollegesList = []
    collegeTypeUrlValue = "/state/city/" + str(city_id)
    collegeFeesUrlValue = "/state/city/" + str(city_id)
    for college in allColleges:
        imagesUrl = list(CollegeImages.objects.filter(college_id=college.id))
        college.college_images_url = imagesUrl
        allCollegesList.append(college)
    state = "/state"
    isListEmpty = False
    if len(allCollegesList) == 0:
        isListEmpty = True
    paginator_obj = Paginator(allCollegesList, number_of_items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator_obj.get_page(page_number)
    return render(request, 'IndianCollegesApp/' + template_name,
                  {'selectedState': selectedState, 'allCitiesList': allCitiesList,
                   'allStatesListForDropdown': allStatesListForDropdown, 'otherThreeStates': otherThreeStates,
                   'isStateNotSelected': isStateNotSelected, 'city_id': city_id, 'state': state,
                   'pageObj': page_obj, 'isListEmpty': isListEmpty,
                   'bottomCardLists': getBottomCardsObjectList(), 'bodyTitle': bodyTitle,
                   'collegeTypeUrlValue': collegeTypeUrlValue, 'feesSelectedLink': selected_link_number,
                   'collegeFeesUrlValue': collegeFeesUrlValue})


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
