from django.conf.urls import url

from earthquake.views import Home

urlpatterns = [
    url(r'', Home.as_view())
]
