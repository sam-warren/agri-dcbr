from django.conf.urls import url

from .views import EmailNotification

urlpatterns = [url("^(?P<email_addr>.+)/$", EmailNotification.as_view())]
