from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
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
    start_date = models.DateField(verbose_name=_('start_date'))
    end_date = models.DateField(verbose_name=_('end_date'))
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


class UniversityInputFieldModel(models.Model):
    UNIVERSITY_INPUT_TYPES = (
        ('checkbox', 'Checkbox'),
        ('text', 'Text'),
    )
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=_('name'))
    input_type = models.CharField(max_length=20, choices=UNIVERSITY_INPUT_TYPES, default='text',
                                  verbose_name=_('input type'))
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('University input')
        verbose_name_plural = _('University inputs')


class BlogModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('slug'))
    image = models.FileField(upload_to='blogs', verbose_name=_('image'))
    short_description = models.TextField(verbose_name=_('Short description'))
    long_description = models.TextField(verbose_name=_('Long description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class ContactModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    year = models.IntegerField()
    location = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    study_location = models.CharField(max_length=100, blank=True)
    BIRTHDAY_MONTH_CHOICES = (
        ('', 'Select your birthday month'),
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    birthday_month = models.CharField(max_length=20, choices=BIRTHDAY_MONTH_CHOICES)

    CELL_CODE_CHOICES = (
        ('', 'Cell / Phone number / Country'),
        ('86', 'China Mainland +86'),
        ('20', 'Egypt +20'),
        ('91', 'India +91'),
        ('234', 'Nigeria +234'),
        ('92', 'Pakistan +92'),
        ('7', 'Russia +7'),
    )
    cell_code = models.CharField(max_length=10, choices=CELL_CODE_CHOICES)

    START_STUDYING_CHOICES = (
        ('', 'When would you like to start studying?'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
    )
    start_studying = models.CharField(max_length=10, choices=START_STUDYING_CHOICES)

    SUBJECT_CHOICES = (
        ('', 'Which subject would you like to study? (optional)'),
        ('L1-Social Sciences', 'Social Sciences and Humanities'),
        ('L1-Business', 'Business and Management'),
        ('L1-Finance', 'Accounting, Economics and Finance'),
        ('L1-Arts', 'Arts'),
        ('L1-Computing', 'Computing and Information Systems'),
        ('L1-Engineering', 'Engineering'),
    )
    subject = models.CharField(max_length=100, blank=True, choices=SUBJECT_CHOICES)

    RESIDENCE_CHOICES = (
        ('', 'Where do you live?'),
        ('CN', 'China Mainland'),
        ('EG', 'Egypt'),
        ('IN', 'India'),
        ('NG', 'Nigeria'),
        ('PK', 'Pakistan'),
    )
    residence = models.CharField(max_length=100, choices=RESIDENCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Payment(models.Model):
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))

    def __str__(self):
        return f"Payment for university: {self.university.title}"

    class Meta:
        verbose_name = _("Paymet")
        verbose_name_plural = _("Payments")
