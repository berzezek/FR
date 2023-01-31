from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .services import get_objects

@csrf_exempt
def index(request):
    form = CustomUserCreationForm(request.POST)
    users = get_objects(User)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('user created')
            return redirect('success')
        else:
            form = CustomUserCreationForm()
    return render(request, 'users/registation.html', {'form': form, 'users': users})

def success(request):
    return render(request, 'users/success.html')