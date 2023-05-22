from django.urls import path
from . import views
from .views import CheckoutListView

app_name = 'auth-us'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('checkout/', CheckoutListView.as_view(), name='checkout'),
    # Другие URL-маршруты вашего приложения
]