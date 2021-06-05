from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path ("", views.index, name = "index"),
    path ("Brian", views.Brian, name = "Brian"),
    path ("David", views.David, name = "David"),
    path ("<str:name>", views.Greet, name = "Greet"),
]