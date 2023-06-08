from django.urls import path
from . import views

urlpatterns = [
    # default path will be hello
    path("", views.index , name="index"),
    path("ryan", views.ryan, name="ryan"),
    path("owi", views.owi, name="owi"),
    path("<str:name>",views.greet,name="greet")
    
]