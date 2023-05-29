from modeltranslation.translator import register, TranslationOptions

from university.models import CountryModel, StudyLevelModel, AdmissionsModel, UniversityModel, BlogModel, \
    UniversityInputFieldModel


@register(CountryModel)
class CountryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(StudyLevelModel)
class StudyTranslationOptions(TranslationOptions):
    fields = ('level',)


@register(AdmissionsModel)
class AdmissionsTranslationOptions(TranslationOptions):
    fields = ('directions',)


@register(UniversityModel)
class UniversityTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'terms_and_conditions',)


@register(UniversityInputFieldModel)
class UniversityInputFieldTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(BlogModel)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)
