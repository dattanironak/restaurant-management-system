from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken !!')
                return redirect('/login/register')
            else:
                user = User(first_name=firstname, last_name=lastname, username=username, email=email)
                user.set_password(password)
                user.save()
                messages.info(request, 'User Created')
                return redirect('/login')
        else:
            messages.info(request, 'Password not matching.')
            return redirect('/login/register')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
