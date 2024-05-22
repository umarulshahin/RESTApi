
from django.urls import path
from Home.views import *
urlpatterns = [
    path('index/',index,name="index"),
    path('person/',PersonData,name="person")
]
