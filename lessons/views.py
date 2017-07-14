from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.template import loader


# Create your views here.
class LessonHome(View):
    template_name = 'lessons.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ssl20(View):
    template_name = 'ssl20.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ssl20Alt1(View):
    template_name = 'ssl20alt1.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ssl20Alt2(View):
    template_name = 'ssl20alt2.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)