from django.shortcuts import render, get_object_or_404
from .models import FashionYear, Trend, StyleIcon


def index(request):
    years = FashionYear.objects.all()
    return render(request, 'pages/index.html', {'years': years})


def era_page(request, year_id):
    years = FashionYear.objects.all()
    current_year = get_object_or_404(FashionYear, id=year_id)
    trends = Trend.objects.filter(fashion_year=current_year)
    icons = StyleIcon.objects.filter(fashion_year=current_year)

    context = {
        'years': years,
        'current_year': current_year,
        'trends': trends,
        'icons': icons
    }
    return render(request, 'pages/era.html', context)


def icon_detail(request, icon_id):
    icon = get_object_or_404(StyleIcon, id=icon_id)
    years = FashionYear.objects.all()
    return render(request, 'pages/icon_detail.html', {'icon': icon, 'years': years})