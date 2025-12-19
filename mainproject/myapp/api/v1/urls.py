# myapp/api/v1/urls.py
from django.urls import path
from .views import profile

urlpatterns = [
    path("profile/", profile),   # final url /api/v1/profile/
]
