from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class Home(View):
    def get(self, request):
        return 'Hello world'


class Upload(View):
    def get(self, request):
        return 'upload'

    def post(self, request):
        return 'posted'


class Chart(View):
    def get(self, request):
        return HttpResponse()

    def post(self, request):
        chart = None
        return HttpResponse(chart)