from django.shortcuts import render

def signup_volunteer(request):
    return render(request, 'registration/signup_volunteer.html')
