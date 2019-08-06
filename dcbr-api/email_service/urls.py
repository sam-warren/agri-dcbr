from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from .views import EmailNotification

urlpatterns = [url("^(?P<user_id>.+)/$", EmailNotification.as_view())]
