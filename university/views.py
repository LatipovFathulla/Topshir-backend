from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.views import View
import requests
from django.shortcuts import get_object_or_404

from university.forms import ContactForm
from university.models import UniversityModel, CountryModel, StudyLevelModel, AdmissionsModel, BlogModel, \
    UniversityInputFieldModel, Payment


class ApplyUniversityView(ListView):
    template_name = 'apply.html'
    paginate_by = 6
    extra_context = {'title': 'Apply University'}
    context_object_name = 'universities'

    def get_queryset(self):
        qs = UniversityModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        country = self.request.GET.get('country')
        level = self.request.GET.get('level')
        admission = self.request.GET.get('admission')
        sort = self.request.GET.get('sort')

        if q:
            qs = qs.filter(title__icontains=q)

        if country:
            qs = qs.filter(country_id=country)

        if level:
            qs = qs.filter(level_id=level)

        if admission:
            qs = qs.filter(admission__id=admission)

        if sort == 'asc':
            qs = qs.order_by('created_at')
        elif sort == 'desc':
            qs = qs.order_by('-created_at')

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = CountryModel.objects.order_by('-pk')
        context['level'] = StudyLevelModel.objects.order_by('-pk')
        context['admission'] = AdmissionsModel.objects.order_by('-pk')

        return context


class UniversityStudentListView(ListView):
    template_name = 'universities.html'
    paginate_by = 6
    extra_context = {'title': 'All Universities'}
    context_object_name = 'stundets_universities'

    def get_queryset(self):
        qs = UniversityModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        country = self.request.GET.get('country')

        if q:
            qs = qs.filter(title__icontains=q)

        if country:
            qs = qs.filter(country_id=country)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = CountryModel.objects.order_by('-pk')

        return context


class UniversityDetailView(DetailView):
    template_name = 'application-program.html'
    model = UniversityModel
    context_object_name = 'university'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        input_fields = UniversityInputFieldModel.objects.filter(university=self.object)
        context['input_fields'] = input_fields
        return context

    def post(self, request, *args, **kwargs):
        university = self.get_object()
        input_fields = UniversityInputFieldModel.objects.filter(university=university)

        for field in input_fields:
            field_name = field.name
            if field.input_type == 'checkbox':
                field.is_checked = field_name in request.POST
            else:
                field.is_checked = False
            print(field)
            field.save()

        redirect_url = self.request.path  # Перенаправляем на текущий URL
        return HttpResponseRedirect(redirect_url)


class BlogListView(ListView):
    template_name = 'blog.html'
    queryset = BlogModel.objects.order_by('-pk')
    extra_context = {'title': 'Blog'}
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'single-blog.html'
    model = BlogModel
    extra_context = {'title': 'Single blog'}


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()  # Сохраняем данные формы в базе данных
            messages.success(request, 'Успешно отправлено!')  # Добавляем сообщение об успешной отправке
            return redirect('pages:contacts')  # Перенаправляем на страницу контактов после успешной отправки
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def callback(request):
    # Получение данных о платеже из запроса
    payment_id = request.GET.get('payment_id')
    status = request.GET.get('status')
    amount = request.GET.get('amount')

    # Получение соответствующего платежа из базы данных
    try:
        payment = Payment.objects.get(payment_id=payment_id)
    except Payment.DoesNotExist:
        return render(request, 'callback-success.html')

    # Проверка статуса платежа и генерация сообщения
    if status == "success":
        message = f"Платеж успешно завершен! Сумма: {amount} USD"
        context = {
            'university': payment.university,
            'amount': payment.amount
        }
        return render(request, 'callback-success.html', context)
    else:
        message = "Ошибка при обработке платежа."

    # Вывод информации о платеже и сообщения
    response = f"Детали платежа:\nУниверситет: {payment.university}\nСумма: {payment.amount} USD\n\n{message}"
    return HttpResponse(response)



def callback_error(request):
    # Получение данных о платеже из запроса
    payment_id = request.GET.get('payment_id')

    # Получение соответствующего платежа из базы данных
    try:
        payment = Payment.objects.get(payment_id=payment_id)
    except Payment.DoesNotExist:
        return render(request, 'callback-error.html')

    # Генерация сообщения об ошибке
    message = "Ошибка при обработке платежа."

    # Вывод информации о платеже и сообщения об ошибке
    context = {
        'university': payment.university,
        'amount': payment.amount,
        'message': message
    }
    return render(request, 'callback-error.html', context)


class PurchaseUniversityView(View):
    def get(self, request, slug):
        university = get_object_or_404(UniversityModel, slug=slug)
        context = {'university': university}
        return render(request, 'checkout.html', context)

    def post(self, request, slug):
        university = get_object_or_404(UniversityModel, slug=slug)
        amount = request.POST.get('amount')

        # Здесь вставьте ваш Sandbox или Production API-ключ и секрет
        api_key = "ECF9746CEFB34166877FC20A32E856E6"
        api_secret = "FC49C3923A14443A8A1969EB391BE19B"

        url = "https://payze.io/api/v1"

        payload = {
            "method": "justPay",
            "apiKey": api_key,
            "apiSecret": api_secret,
            "data": {
                "amount": amount,
                "currency": "USD",
                "callback": request.build_absolute_uri(reverse('uni:callback')),
                "callbackError": request.build_absolute_uri(reverse('uni:callback_error')),
                "preauthorize": False,
                "lang": "RU",
                "hookUrlV2": "https://corp.com/payze_hook?authorization_token=token",
                "info": {
                    "description": f"Payment for university: {university.title}",
                    "image": "https://payze.io/assets/images/logo_v2.svg",
                    "name": "University Payment"
                },
                "hookRefund": False
            }
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            payment_id = response.json().get('data', {}).get('paymentId')

            # Сохранение информации о платеже в базе данных
            payment = Payment.objects.create(
                university=university,
                amount=amount,
                payment_id=payment_id
            )

            # Перенаправление пользователя на страницу оплаты
            return HttpResponseRedirect(response.json().get('response', {}).get('transactionUrl'))
        else:
            # Обработка ошибки при создании платежа
            error_message = response.json().get('message', 'Payment creation failed.')
            return HttpResponseServerError('Payment creation failed.')
