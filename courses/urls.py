from django.urls import path
from .views import get_course, index

urlpatterns = [
    path("",index,name="home"),
    path("courses/",get_course,name="course"),
]
