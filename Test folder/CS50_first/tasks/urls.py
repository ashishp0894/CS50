from django.urls import path
from django.urls.resolvers import URLPattern

from .import views
app_name = "tasks"

urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.add,name="add"),

]