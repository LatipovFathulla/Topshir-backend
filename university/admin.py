from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from university.models import CountryModel, StudyLevelModel, AdmissionsModel, UniversityModel, BlogModel, \
    UniversityInputFieldModel, ContactModel


class MyNewTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CountryModel)
class CountryModelAdmin(MyNewTranslationAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']


@admin.register(StudyLevelModel)
class StudyLevelModelAdmin(MyNewTranslationAdmin):
    list_display = ['id', 'level', 'created_at', 'updated_at']


@admin.register(AdmissionsModel)
class AdmissionsModelAdmin(MyNewTranslationAdmin):
    list_display = ['id', 'start_date', 'end_date', 'directions', 'created_at', 'updated_at']


@admin.register(UniversityModel)
class UniversityModelAdmin(MyNewTranslationAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(UniversityInputFieldModel)
class UniversityInputFieldModelAdmin(MyNewTranslationAdmin):
    list_display = ['name', 'is_checked']


@admin.register(BlogModel)
class BlogModelAdmin(MyNewTranslationAdmin):
    list_display = ['id', 'title', 'short_description', 'created_at', 'updated_at']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'location']
