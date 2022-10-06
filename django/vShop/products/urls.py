from django.urls import path
from . import views  # using the period here specifies that the import is from the current folder only


urlpatterns = [
    path("", views.index),  # The empty strings "" represents the root of this App
    path("new", views.new),
    path("categories", views.categories)
]

