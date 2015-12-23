from django.conf.urls import url

from core.views import AppList

urlpatterns = [
    url(r'^$', AppList.as_view())
]
