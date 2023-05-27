from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.

def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        mail = User.objects.get(email=email)
        print(mail.username)

        user = auth.authenticate(username = mail.username, password = password)
        # user.is_authenticated
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Given Credentials are Invalid')
            return redirect('/')
    else:
        return render(request, 'loginpage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        # number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already used')
            return redirect('signup')
        # elif User.objects.filter(number=number).exists():
        #     messages.info(request,"Number already used")
        #     return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already used')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username,email=email,password = password)
            user.save()
            return redirect('/')
    else:
        return render(request, 'signup.html')
    
def home(request):
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')