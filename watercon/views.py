from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView

from watercon.models import WaterConYear


class Home(View):
    template_name = 'watercon/home.html'

    def get(self, request):
        return render(request, self.template_name)


class Upload(View):
    def get(self, request):
        return HttpResponse('upload')

    def post(self, request):

        return HttpResponse('posted')


class Chart(View):
    def get(self, request):
        return HttpResponse()

    def post(self, request):
        chart = None
        return HttpResponse(chart)


class WaterConByYear(ListView):
    template_name = 'watercon/waterconmodel.html'
    model = WaterConYear
