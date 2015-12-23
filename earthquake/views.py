from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class Home(View):
    def get(self, request):
        return HttpResponse('Earthquake application')


class UploadDataBase(View):
    def get(self, request):
        # current = None
        return render(request, 'earthquake/upload', context=current)

    def post(self, request):
        return json()