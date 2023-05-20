from ckeditor.fields import RichTextField
from django.db import models
from slugify import slugify
from django.utils.translation import gettext_lazy as _


class CountryModel(models.Model):
    title = models.CharField(max_length=90, verbose_name=_('title'))
    image = models.FileField(upload_to='images/country', verbose_name=_('image'), null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class StudyLevelModel(models.Model):
    level = models.CharField(max_length=90, verbose_name=_('level'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = _('Study Level')
        verbose_name_plural = _('Study Levels')


class AdmissionsModel(models.Model):
    start_date = models.DateField(verbose_name=_('date'))
    end_date = models.DateField(verbose_name=_('date'))
    directions = models.TextField(verbose_name=_('directions'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.directions

    class Meta:
        verbose_name = _('Admission')
        verbose_name_plural = _('Admissions')


class UniversityModel(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('slug'))
    logo = models.FileField(upload_to='university', verbose_name=_('logo'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, verbose_name=_('country'))
    level = models.ForeignKey(StudyLevelModel, on_delete=models.CASCADE, verbose_name=_('level'))
    admission = models.ManyToManyField(AdmissionsModel, verbose_name=_('admission'))
    terms_and_conditions = models.TextField(verbose_name=_('Terms and Conditions'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('University')
        verbose_name_plural = _('Universities')

