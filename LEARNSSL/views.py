from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.template import loader


# Create your views here.
class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
