from django.views.generic import ListView

from university.models import UniversityModel, CountryModel, StudyLevelModel, AdmissionsModel


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
            qs = qs.filter(admission_id=admission)

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

