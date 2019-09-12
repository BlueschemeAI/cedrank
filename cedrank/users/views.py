from django.shortcuts import render, redirect
from users.forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            if User.objects.filter(email=user.email).exists():
                messages.error(request, f'Your Email already exist')
                return redirect("signup")
            else:
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                #profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered = True
                if user and profile:
                    subject = 'Thank you for registering to our site'
                    message = ' Welcome to Credrank \n Thank you for registration '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email]
                    send_mail(subject, message, email_from, recipient_list)
                    messages.error(request, f'Your account has been created. Please login.')
                    return redirect("login")
                else:
                    messages.error(request, f'Your Email already exist')
                    return redirect("signup")
        else:
            messages.error(request, f'Your username already exist')
            return redirect("signup")
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            get_user_name = User.objects.get(email=email)
            user = authenticate(username=get_user_name, password=password)
            if user:
                if user.is_active:
                #login(request,user)
                    return redirect("debtors")
                else:
                    messages.error(request, f'Your account was inactive.')
                    return redirect("login")        
            else:
                messages.error(request, f'Invalid login details')
                return redirect("login")
        except:
            messages.warning(request, f'Invalid login details')
            return redirect("login")
    else:
        return render(request, 'login.html', {})

def creditors(request):
    return render(request, 'creditors.html', {})
