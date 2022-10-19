from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import (authenticate, get_user_model, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings

from .models import AppUsers
from .forms import LoginForm, UpdateUserForm ,UpdateAppUserForm


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
                    login(request, user)
                    request.session['session'] = user.pk
                    return redirect('home')
        else:
            error_message = 'Invalid username or password'
            messages.error(request,"Invalid username or password.")      

    form = LoginForm()
    return render(request, "registration/login.html", context={"form":form,})
def logout_page(request):
    logout(request)

    return redirect('home')
    
# @login_required
# def home_page(request):
    
#     return render(request, "userportfolio/home.html", context={})

@login_required
def view_details(request):
    if request.method == 'POST':
        return redirect('home')
    
    current_user = request.user
    user_details = request.user.appusers
    context = {'user': current_user, 'user_details':user_details}
    
    return render(request, 'userportfolio/view_details.html', context)

@login_required      
def details_page(request):
    current_user = request.user
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateAppUserForm(request.POST, instance=request.user.appusers)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='home')
    
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateAppUserForm(instance=request.user.appusers)
    context = {'user': current_user, 'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'userportfolio/edit_details.html', context)

@method_decorator(login_required, name='dispatch')
class home_page(CreateView):

    model = AppUsers
    fields = ['home_address']
    template_name = 'userportfolio/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = getattr(settings, "MAPBOX_ACCESS_TOKEN", None)
        context['users'] = AppUsers.objects.all()
        context['current_user'] = self.request.user
        return context
