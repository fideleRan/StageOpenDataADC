# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    #Journal page
    path('Journal', views.journal, name="jrnl"),
    
    #Contributeur page
    path('Contributeur', views.contributeur, name="contrib"),
    
    # The home page
    path('Accueil', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
