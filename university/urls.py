from django.urls import path

from university.views import ApplyUniversityView, UniversityDetailView, UniversityStudentListView, BlogListView, \
    BlogDetailView

app_name = 'uni'

urlpatterns = [
    path('apply/', ApplyUniversityView.as_view(), name='apply'),
    path('apply/universities/', UniversityStudentListView.as_view(), name='stundets_universities'),
    path('apply/<slug:slug>/', UniversityDetailView.as_view(), name='single'),
    path('blog', BlogListView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='single-blogs')
]
