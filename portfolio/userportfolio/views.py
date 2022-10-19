from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import (authenticate, get_user_model, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User

from .models import AppUsers
from .forms import LoginForm


@csrf_exempt
def login_page(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if 'login' in request.POST:
                if user is not None:
                    request.session['session'] = user.pk
                    return redirect('home')
        else:
            error_message = 'Invalid username or password'
            messages.error(request,"Invalid username or password.")      

    form = LoginForm()
    return render(request, "registration/login.html", context={"form":form,})

def home_page(request):
    
    return render(request, "userportfolio/home.html", context={})
    

class UserView(CreateView):

    model = AppUsers
    fields = ['']
    template_name = ''
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = AppUsers.objects.all()
        return context
