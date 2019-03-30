from django.urls import path, include
from .views import LeadListCreate

urlpatterns = [
    path('', LeadListCreate.as_view()),
]