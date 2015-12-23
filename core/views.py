from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from appslangleytk.settings import MY_APPS


class AppList(View):
    template_name = 'core/applist.html'

    def get(self, request):
        return render(request, self.template_name, context={
            'app_list': MY_APPS,
        })