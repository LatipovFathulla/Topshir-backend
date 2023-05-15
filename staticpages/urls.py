from django.urls import path

from staticpages.views import HomeTemplateView, AboutIntoTemplateView, SuccessIntoTemplateView, FaqTemplateView, \
    StudyAbroadTemplateView, StudyProgramsTemplateView, StudyIntoTemplateView, AdmissionsTemplateView, \
    ContactTemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about-into/', AboutIntoTemplateView.as_view(), name='about'),
    path('success-into/', SuccessIntoTemplateView.as_view(), name='success'),
    path('faq/', FaqTemplateView.as_view(), name='FAQ'),
    path('study-abroad/', StudyAbroadTemplateView.as_view(), name='study-abroad'),
    path('study-programs/', StudyProgramsTemplateView.as_view(), name='study-programs'),
    path('choise-into/', StudyIntoTemplateView.as_view(), name='choice-into'),
    path('admissions/', AdmissionsTemplateView.as_view(), name='admissions'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
]
