from django.urls import path 
from .views import HomeList

urlpatterns = [
    path('', HomeList.as_view()),
]