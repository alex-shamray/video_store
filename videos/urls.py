from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.VideoList.as_view()),
]
