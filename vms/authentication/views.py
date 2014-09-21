from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world")
    
def login_process(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect('/AdminUnit/')
                return HttpResponse('You have successfully logged in!')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        if request.user.is_authenticated():
            #return HttpResponseRedirect('AdminUnit/index/')
            return HttpResponse('You are logged in!')
        return render(request, 'authentication/login.html')

@login_required
def logout_process(request):

    logout(request)
    return HttpResponseRedirect('/AdminUnit/')
