from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include  # add this

def journal(request):
    return render(request , "home/Journal.html")

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    path("contributeur/", include("apps.contributeur.urls"))
]
