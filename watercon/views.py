from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from watercon.forms import InputCSVForm
from watercon.models import WaterConYear, UploadedCSV


class Home(View):
    template_name = 'watercon/home.html'

    def get(self, request):
        return render(request, self.template_name)


class UploadedCSVList(ListView):
    template_name = 'watercon/csvlist.html'
    model = UploadedCSV


class Upload(View):
    def get(self, request):
        return HttpResponse('upload')

    def post(self, request):
        form = InputCSVForm(request.POST)
        print request.POST
        print request.FILES
        if form.is_valid():
            new_doc = UploadedCSV(name=form.cleaned_data['name'], file=form.cleaned_data['csv_file'])
            new_doc.save()
            return redirect(reverse('watercon.views.'))
        else:
            return redirect('upload_csv')


class Chart(View):
    def get(self, request):
        return HttpResponse()

    def post(self, request):
        chart = None
        return HttpResponse(chart)


class WaterConByYear(ListView):
    template_name = 'watercon/waterconmodel.html'
    model = WaterConYear
