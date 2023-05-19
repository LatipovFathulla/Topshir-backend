from django.urls import path

from university.views import ApplyUniversityView

app_name = 'uni'

urlpatterns = [
    path('apply/', ApplyUniversityView.as_view(), name='apply')
]
