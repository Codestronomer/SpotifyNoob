from django.urls import path
from . import views

# Urls patterns
urlpatterns = [
    path("/", views.index, name="home"),
]
