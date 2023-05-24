from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from university.models import UniversityModel, CountryModel, BlogModel


class HomeTemplateView(ListView):
    template_name = 'index.html'
    extra_context = {'title': 'Topshir Uz | Study Abroad'}
    paginate_by = 6
    context_object_name = 'homes'

    def get_queryset(self):
        qs = UniversityModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        country = self.request.GET.get('country')

        if q:
            qs = qs.filter(title__icontains=q)

        if country:
            qs = qs.filter(country_id=country)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = CountryModel.objects.order_by('-pk')
        context['blogs'] = BlogModel.objects.order_by('-pk')
        return context


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


class UKTemplateView(TemplateView):
    template_name = 'uk.html'
    extra_context = {'title': 'UK'}


class USATemplateView(TemplateView):
    template_name = 'us.html'
    extra_context = {'title': 'USA'}


class AustraliaTemplateView(TemplateView):
    template_name = 'australia.html'
    extra_context = {'title': 'Australia'}


class LanguageTemplateView(TemplateView):
    template_name = 'language.html'
    extra_context = {'title': 'Language'}


class CultureTemplateView(TemplateView):
    template_name = 'culture.html'
    extra_context = {'title': 'Culture'}
