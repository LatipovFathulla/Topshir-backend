from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView

from university.models import UniversityModel, CountryModel, StudyLevelModel, AdmissionsModel, BlogModel, \
    UniversityInputFieldModel


class ApplyUniversityView(ListView):
    template_name = 'apply.html'
    paginate_by = 6
    extra_context = {'title': 'Apply University'}
    context_object_name = 'universities'

    def get_queryset(self):
        qs = UniversityModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        country = self.request.GET.get('country')
        level = self.request.GET.get('level')
        admission = self.request.GET.get('admission')
        sort = self.request.GET.get('sort')

        if q:
            qs = qs.filter(title__icontains=q)

        if country:
            qs = qs.filter(country_id=country)

        if level:
            qs = qs.filter(level_id=level)

        if admission:
            qs = qs.filter(admission__id=admission)

        if sort == 'asc':
            qs = qs.order_by('created_at')
        elif sort == 'desc':
            qs = qs.order_by('-created_at')

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = CountryModel.objects.order_by('-pk')
        context['level'] = StudyLevelModel.objects.order_by('-pk')
        context['admission'] = AdmissionsModel.objects.order_by('-pk')

        return context


class UniversityStudentListView(ListView):
    template_name = 'universities.html'
    paginate_by = 6
    extra_context = {'title': 'All Universities'}
    context_object_name = 'stundets_universities'

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

        return context


class UniversityDetailView(DetailView):
    template_name = 'application-program.html'
    model = UniversityModel
    context_object_name = 'university'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        input_fields = UniversityInputFieldModel.objects.filter(university=self.object)
        context['input_fields'] = input_fields
        return context

    def post(self, request, *args, **kwargs):
        university = self.get_object()
        input_fields = UniversityInputFieldModel.objects.filter(university=university)

        for field in input_fields:
            field_name = field.name
            if field.input_type == 'checkbox':
                field.is_checked = field_name in request.POST
            else:
                field.is_checked = False
            field.save()

        redirect_url = self.request.path  # Перенаправляем на текущий URL
        return HttpResponseRedirect(redirect_url)

class BlogListView(ListView):
    template_name = 'blog.html'
    queryset = BlogModel.objects.order_by('-pk')
    extra_context = {'title': 'Blog'}
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'single-blog.html'
    model = BlogModel
    extra_context = {'title': 'Single blog'}
