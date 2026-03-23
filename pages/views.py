from django.shortcuts import render, get_object_or_404
from .models import FashionYear, Trend, StyleIcon


# В'юшка для головної сторінки
def index(request):
    # Дістаємо всі роки з бази, щоб показати їх у меню (хедері)
    years = FashionYear.objects.all()
    return render(request, 'pages/index.html', {'years': years})


# В'юшка для сторінки конкретної епохи
def era_page(request, year_id):
    years = FashionYear.objects.all()  # Знову дістаємо роки для меню

    # Шукаємо конкретний рік по його ID
    current_year = get_object_or_404(FashionYear, id=year_id)

    # Шукаємо тренди та ікони стилю, які прив'язані саме до цього року
    trends = Trend.objects.filter(fashion_year=current_year)
    icons = StyleIcon.objects.filter(fashion_year=current_year)

    # Пакуємо все в словник і передаємо в HTML
    context = {
        'years': years,
        'current_year': current_year,
        'trends': trends,
        'icons': icons
    }
    return render(request, 'pages/era.html', context)