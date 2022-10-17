# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import inscription, authentification, logoutUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('login/', login_view, name="login"),
    # path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("inscription/<str:pk>/", inscription, name="inscription"),
    path("authentification/", authentification, name="authentificaton"),
    path("deconnexion/", logoutUser, name="deconnexion")
]
