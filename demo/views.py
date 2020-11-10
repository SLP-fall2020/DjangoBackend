from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Course
# Create your views here.
class info(View):
    def get(self, request):
        courses = Course.objects.all()

        output = f"We have this many courses in our DB"

        return HttpResponse(self.output)
