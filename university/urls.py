from django.urls import path

from university.views import ApplyUniversityView, UniversityDetailView, UniversityStudentListView, BlogListView, \
    BlogDetailView, PurchaseUniversityView, callback, callback_error

app_name = 'uni'

urlpatterns = [
    path('apply/', ApplyUniversityView.as_view(), name='apply'),
    path('apply/universities/', UniversityStudentListView.as_view(), name='stundets_universities'),
    path('apply/<slug:slug>/', UniversityDetailView.as_view(), name='single'),
    path('blog', BlogListView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='single-blogs'),
    path('apply/<slug:slug>/purchase/', PurchaseUniversityView.as_view(), name='purchase'),
    path('callback/', callback, name='callback'),
    path('callback-error/', callback_error, name='callback_error'),

]
