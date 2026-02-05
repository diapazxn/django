from django.contrib import admin
from django.urls import path, include  # <-- Не забудь додати include сюди!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # <-- Підключаємо наші сторінки
]