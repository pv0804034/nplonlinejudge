from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from programmers.models import Profile
# Create your views here.


def otherprofile(request, _id):
    userid = _id
    usercore = User.objects.filter(id=userid)
    userprofile = Profile.objects.filter(user_id=userid)
    if usercore.exists() and userprofile.exists():
        usercoreobject = usercore[0]
        userprofileobject = userprofile[0]
    else:
        usercoreobject = ''
        userprofileobject = ''
    return render(request, 'programmers/profile.html', {'usercore': usercoreobject, 'userprofile': userprofileobject})


def profile(request):
    if request.user.is_authenticated:
        userid = request.user.id
        usercore = User.objects.filter(id=userid)
        userprofile = Profile.objects.filter(user_id=userid)
        if usercore.exists() and userprofile.exists():
            usercoreobject = usercore[0]
            userprofileobject = userprofile[0]
        else:
            usercoreobject = ''
            userprofileobject = ''
    else:
        usercoreobject = ''
        userprofileobject = ''
    return render(request, 'programmers/profile.html', {'usercore': usercoreobject, 'userprofile': userprofileobject})


def logout(request):
    auth.logout(request)
    return redirect('index')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # valid user
            auth.login(request, user)
            return redirect('/')
        else:
            # invalid user
            messages.warning(request, 'Invalid username/password')
            return redirect('login')
    else:
        return render(request, 'programmers/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        gooduser = True
        if password1 != password2:
            messages.warning(request, 'Passwords not matching')
            gooduser = False
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already taken')
            gooduser = False
        elif User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already taken')
            gooduser = False
        if not gooduser:
            return redirect('register')
        else:
            # create a User() object
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=firstname,
                last_name=lastname,
            )
            user.save()
            # create the appropriate user profile
            profile = Profile(user=user)
            # save the profile
            profile.save()
            messages.success(request, 'Signup Successful!')
            return redirect('login')
    else:
        return render(request, 'programmers/register.html')
