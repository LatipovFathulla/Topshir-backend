from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Topshir Uz | Study Abroad'}


class AboutIntoTemplateView(TemplateView):
    template_name = 'about-into.html'
    extra_context = {'title': 'About INTO'}


class SuccessIntoTemplateView(TemplateView):
    template_name = 'success-with.html'
    extra_context = {'title': 'Success INTO'}


class FaqTemplateView(TemplateView):
    template_name = 'faq.html'
    extra_context = {'title': 'FAQ'}


class StudyAbroadTemplateView(TemplateView):
    template_name = 'study-abroad.html'
    extra_context = {'title': 'Study Abroad'}


class StudyProgramsTemplateView(TemplateView):
    template_name = 'study-programs.html'
    extra_context = {'title': 'Study Programs'}


class StudyIntoTemplateView(TemplateView):
    template_name = 'choice-page.html'
    extra_context = {'title': 'Choice | Into'}


class AdmissionsTemplateView(TemplateView):
    template_name = 'admissions.html'
    extra_context = {'title': 'Admissions | Topshir'}


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
    extra_context = {'title': 'Contacts'}
