from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class AppList(View):
    def get(self, request):
        return HttpResponse('list of apps')