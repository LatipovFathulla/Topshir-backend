# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, TemplateView

from university.models import UniversityModel


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        last_name = request.POST['last_name']

        if not User.objects.filter(username=username).exists():
            # Создаем нового пользователя
            user = User.objects.create_user(username=username, password=password, last_name=last_name)

            # Входим в систему после регистрации
            login(request, user)

            # Перенаправляем на главную страницу или другую нужную страницу
            return redirect('/')
        else:
            # Если пользователь с таким именем уже существует, выводим сообщение об ошибке
            error_message = 'Пользователь с таким именем уже существует'
            return render(request, 'sign-up.html', {'error_message': error_message})

    return render(request, 'sign-up.html')


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


def logout_view(request):
    logout(request)
    return redirect('auth-us:login')
