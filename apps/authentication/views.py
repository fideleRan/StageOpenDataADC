# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import InscriptionForm


# def login_view(request):
#     form = LoginForm(request.POST or None)

#     msg = None

#     if request.method == "POST":

#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("/")
#             else:
#                 msg = 'Invalid credentials'
#         else:
#             msg = 'Error validating the form'

#     return render(request, "accounts/login.html", {"form": form, "msg": msg})


# def register_user(request):
#     msg = None
#     success = False

#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'User created successfully.'
#             success = True

#             # return redirect("/login/")

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()

#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})



def inscription(request):
    msg = ""
    form = InscriptionForm()
    if request.method == "POST":
        form = InscriptionForm(data=request.POST)
        if form.is_valid():
            form.save()
            print("save")
            msg = "saved"
            return redirect("/authentification/")
            
        else:
            print("unsave")
            msg = "unsaved"

    context = {
        'form' : form,
        'msg' : msg
    }

    return render(request, "accounts/inscription.html", context=context)

def authentification(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_adminUser:
                return redirect("/adminUser/journal/")
            
            elif user.is_contributeur:
                return redirect("/contributeur/accueil/")

        else:
            error = "Invalide authentication!"

    context = {
        'error' : error
    }

    return render(request, "accounts/authentification.html", context=context)
