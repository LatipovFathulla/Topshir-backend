from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class ApplyUniversityView(TemplateView):
    template_name = 'apply.html'
