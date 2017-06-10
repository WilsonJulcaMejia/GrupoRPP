__author__ = 'lucaru9'

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^news/$', ListNewsAPI.as_view()),
]
