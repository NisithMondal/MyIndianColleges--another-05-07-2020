from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def signIn(request):
    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'This Email Address Already Exists')
            return render(request, 'SignInApp/sign_in.html', {'isPostRequest': True, 'firstName': firstName, 'lastName': lastName,
                                                              'email': email, 'password': password})
        else:
            newUser = User.objects.create_user(username=email, first_name=firstName, last_name=lastName, email=email, password=password)
            newUser.save()
            return render(request, 'SignInApp/login.html')

    else:
        return render(request, 'SignInApp/sign_in.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Email and Password Does Not Exists')
            return render(request, 'SignInApp/login.html', {'isPostRequest': True, 'email': email, 'password': password})

    else:
        return render(request, 'SignInApp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
