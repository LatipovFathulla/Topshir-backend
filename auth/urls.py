from django.urls import path
from . import views
from .views import CheckoutListView, ProfileListView, logout_view

app_name = 'auth-us'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('checkout/', CheckoutListView.as_view(), name='checkout'),
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('logout/', logout_view, name='logout'),
    # Другие URL-маршруты вашего приложения
]