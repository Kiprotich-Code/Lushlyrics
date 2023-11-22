from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.
def login_listener(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('Login Successful'))
            return redirect('home')
        
        else:
            messages.success(request, ('Enter Valid Details'))
            return redirect('login')
    else:
        return render(request, 'listeners/login.html', {})
    

def register_listener(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, ("Registered Sucessful"))
            return redirect('login')
    else:   
        form = RegisterUserForm()
    
    return render(request, 'listeners/signup.html', {'form': form})

def logout_listener(request):
    messages.success(request, (f"See you again!"))
    logout(request)
    return redirect('login')