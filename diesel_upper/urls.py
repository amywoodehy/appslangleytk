from django.conf.urls import url

from diesel_upper.views import Home

urlpatterns = [
    url(r'', Home.as_view())
]
