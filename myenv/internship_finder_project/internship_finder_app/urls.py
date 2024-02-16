from django.urls import path
from . import views

urlpatterns = [
    path('internship_finder_app/', views.internship_finder_app, name='internship_finder_app'),
]