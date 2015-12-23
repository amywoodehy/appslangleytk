from django.conf.urls import url, include
from django.views.generic import TemplateView

from watercon import views

# upload_pattern = [
#     url(r'^$', views.Upload.as_view(), name='Upload'),
#     url(r'^csv/$', views.Upload.as_view(), name='Upload CSV'),
# ]

urlpatterns = [
    url(r'upload_csv$', TemplateView.as_view(template_name='watercon/upload_csv.html'), name='upload_csv'),
    url(r'^upload$', views.Upload.as_view(), name='upload'),
    url(r'^book$', TemplateView.as_view(template_name='watercon/book.html'), name='book'),
    url(r'^jupyter$', TemplateView.as_view(template_name='watercon/jupyter_notebook.html'), name='jupyter'),
    url(r'^$', views.Home.as_view(), name='Home'),
    url(r'^models/watercon$', views.WaterConByYear.as_view(), name='waterconmodel'),
]
