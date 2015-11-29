from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class Home(View):
    def get(self):
        return HttpResponse('Diesel upper application')