from django.conf.urls import include, url
from django.contrib import admin
from coleyoungmark.views import landingpage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', landingpage),
]

urlpatterns += staticfiles_urlpatterns()
