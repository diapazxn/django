from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('era/<int:year_id>/', views.era_page, name='era_page'),
    path('icon/<int:icon_id>/', views.icon_detail, name='icon_detail'),
]