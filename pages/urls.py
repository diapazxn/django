from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # Цей шлях буде ловити ID року (наприклад, /era/1/)
    path('era/<int:year_id>/', views.era_page, name='era_page'),
]