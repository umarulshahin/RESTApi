
from django.urls import path,include
from Home.views import *
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register(r'people',PeopleViewSets,basename="people")


urlpatterns = [
    path('',include(router.urls)),
    path('index/',index,name="index"),
    path('person/',PersonData,name="person"),
    path('classPerson/',ClassPerson.as_view(),name="classPerson"),
    path("register/",RegisterApi.as_view(),name="register"),
    path("login/",LoginApi.as_view(),name="login"),
    path('peopleAuth/',peopleAuth.as_view(),name="peopleAuth"),
]
