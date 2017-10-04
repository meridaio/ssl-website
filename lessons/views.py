from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.staticfiles.templatetags.staticfiles import static
import json
import os


# Create your views here.
class LessonHome(View):
    template_name = 'lessons.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ssl20(View):
    template_name = 'ssl20.html'
    # packets_json = static('LEARNSSL/ssl2packets.json')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_url = static('LEARNSSL/ssl2packets.json')
    packets_json = os.path.join(base_dir, static_url[1:])
    # Might cause problems in deployment? some backslash some forward slash in packets_json
    # Python doesn't seem to care though

    def get(self, request):
        with open(self.packets_json) as data_file:
            data = json.load(data_file)
        context = {'json': data, 'test': {'name': 'Nathan', 'age': 21}}
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, context)


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