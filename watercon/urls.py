from django.conf.urls import url
from django.views.generic import TemplateView

from watercon import views


urlpatterns = [
    url(r'^book', TemplateView.as_view(template_name='watercon/book.html'), name='book'),
    url(r'^jupyter', TemplateView.as_view(template_name='watercon/jupyter_notebook.html'), name='jupyter'),
    url(r'^$', views.Home.as_view(), name='Home'),
]
