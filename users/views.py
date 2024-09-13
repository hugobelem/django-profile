from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm

def signup(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower().strip()
            user.save()
            login(request, user)
            return redirect('users:home')

    return render(request, 'signup.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'home.html'
