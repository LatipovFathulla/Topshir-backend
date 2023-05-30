from django.urls import path

from staticpages.views import HomeTemplateView, AboutIntoTemplateView, SuccessIntoTemplateView, FaqTemplateView, \
    StudyAbroadTemplateView, StudyProgramsTemplateView, StudyIntoTemplateView, AdmissionsTemplateView, \
    ContactTemplateView, UKTemplateView, USATemplateView, AustraliaTemplateView, LanguageTemplateView, \
    CultureTemplateView
from university.views import contact

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
    path('contacts/', contact, name='contacts'),
    path('UK/', UKTemplateView.as_view(), name='uk'),
    path('USA/', USATemplateView.as_view(), name='usa'),
    path('Australia/', AustraliaTemplateView.as_view(), name='australia'),
    path('language/', LanguageTemplateView.as_view(), name='language'),
    path('culture/', CultureTemplateView.as_view(), name='culture'),
]
