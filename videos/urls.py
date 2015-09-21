from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/rent$', views.VideoRent.as_view()),
    url(r'^(?P<pk>[0-9]+)/return$', views.VideoReturn.as_view()),
    url(r'^(?P<keyword>.*)$', views.VideoList.as_view()),
]
