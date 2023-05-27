# views.py
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, TemplateView
from university.models import UniversityModel
from twilio.rest import Client


def generate_verification_code():
    # Генерация рандомного четырехзначного кода
    return str(random.randint(1000, 9999))


def send_verification_code(phone_number, verification_code):
    # Ваши данные учетной записи Twilio
    account_sid = 'AC39dfd8ebcbfa83fb47416c784187dfc5'
    auth_token = 'b1306e46326087eb6b270bbc1debf32c'
    twilio_phone_number = '+13158722352'  # Ваш номер Twilio

    # Создание клиента Twilio
    client = Client(account_sid, auth_token)

    # Отправка SMS-сообщения с кодом подтверждения
    client.messages.create(
        body=f'Ваш код подтверждения: {verification_code}',  # Замените на ваш код подтверждения
        from_=twilio_phone_number,
        to=phone_number
    )


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        last_name = request.POST['last_name']

        if not User.objects.filter(username=username).exists():
            # Создаем нового пользователя
            user = User.objects.create_user(username=username, password=password, last_name=last_name)

            verification_code = generate_verification_code()

            # Отправляем код подтверждения
            send_verification_code(username, verification_code)

            # Сохраняем код подтверждения и имя пользователя в сессии
            request.session['verification_code'] = verification_code
            request.session['username'] = username

            # Перенаправляем на страницу подтверждения
            return redirect('auth-us:confirmation')
        else:
            # Если пользователь с таким именем уже существует, выводим сообщение об ошибке
            error_message = 'Пользователь с таким именем уже существует'
            return render(request, 'sign-up.html', {'error_message': error_message})

    return render(request, 'sign-up.html')


def confirmation(request):
    if request.method == 'POST':
        verification_code = request.POST['verification_code']
        stored_verification_code = request.session.get('verification_code')
        username = request.session.get('username')

        if verification_code == stored_verification_code:
            # Удаляем код подтверждения из сессии
            del request.session['verification_code']

            # Попытка аутентификации пользователя
            user = User.objects.filter(username=username).first()

            if user is not None:
                # Аутентификация пользователя
                login(request, user)
                return redirect('/')
            else:
                error_message = 'Ошибка аутентификации'
        else:
            # Если код подтверждения неправильный, выводим сообщение об ошибке
            error_message = 'Неправильный код подтверждения'
    else:
        error_message = ''

    return render(request, 'confirmation.html', {'error_message': error_message})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Аутентифицируем пользователя
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Входим в систему
            login(request, user)

            # Перенаправляем на главную страницу или другую нужную страницу
            return redirect('/')
        else:
            # Если аутентификация не удалась, выводим сообщение об ошибке
            error_message = 'Неверные имя пользователя или пароль'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('auth-us:login')


class CheckoutListView(TemplateView):
    template_name = 'checkout.html'
    extra_context = {'title': 'Checkout'}


class ProfileListView(TemplateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Profile'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stundets_universities'] = UniversityModel.objects.order_by('-pk')

        return context
