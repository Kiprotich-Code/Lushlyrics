from django.shortcuts import render

# Create your views here.
def login_listener(request):
    return render(request, 'listeners/login.html')