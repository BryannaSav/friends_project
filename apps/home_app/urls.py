# LOGIN ROUTE
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^addFriend/(?P<id>\d+)$', views.addFriend),
    url(r'^removeFriend/(?P<id>\d+)$', views.removeFriend),
    url(r'^show/(?P<id>\d+)$', views.show),
]