"""appslangleytk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from earthquake import urls as quake_url
from diesel_upper import urls as dieselupper_url
from dilemma import urls as dilemma_url
from forgive import urls as forgive_url
from poll import urls as poll_url
from quine import urls as quine_url
from quizer import urls as quizer_url
from core import urls as core_urls
from watercon import url as watercon_url


urlpatterns = [
    url(r'^$', include(core_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^earthquake/', include(quake_url)),
    # url(r'^quizer/', include(quizer_url)),
    # url(r'^dilemma/', include(dilemma_url)),
    url(r'^diesel_upper/', include(dieselupper_url)),
    url(r'^watercon/', include(watercon_url)),
    # url(r'^poll/', include(poll_url)),
    # url(r'^forgive/', include(forgive_url)),
    # url(r'^quine/', include(quine_url)),
]
