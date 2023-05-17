from django.contrib import admin

from university.models import CountryModel, StudyLevelModel, AdmissionsModel, UniversityModel


@admin.register(CountryModel)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']


@admin.register(StudyLevelModel)
class StudyLevelModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'level', 'created_at', 'updated_at']


@admin.register(AdmissionsModel)
class AdmissionsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'directions', 'created_at', 'updated_at']


@admin.register(UniversityModel)
class UniversityModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'country', 'created_at', 'updated_at']
