from django.urls import path

from university.views import ApplyUniversityView, UniversityDetailView

app_name = 'uni'

urlpatterns = [
    path('apply/', ApplyUniversityView.as_view(), name='apply'),
    path('apply/<slug:slug>/', UniversityDetailView.as_view(), name='single')
]
