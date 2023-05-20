from django.urls import path

from university.views import ApplyUniversityView, UniversityDetailView, UniversityStudentListView

app_name = 'uni'

urlpatterns = [
    path('apply/', ApplyUniversityView.as_view(), name='apply'),
    path('apply/universities/', UniversityStudentListView.as_view(), name='stundets_universities'),
    path('apply/<slug:slug>/', UniversityDetailView.as_view(), name='single')
]
