from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post, name='myPage'),
    url(r'course_id=\d', views.get, name='CourseData'),
]
