from django.contrib import admin
from .models import FashionYear, Trend, StyleIcon

@admin.register(FashionYear)
class FashionYearAdmin(admin.ModelAdmin):
    # Вказуємо, які колонки показувати в списку
    list_display = ('year', 'created_at', 'updated_at')

@admin.register(Trend)
class TrendAdmin(admin.ModelAdmin):
    list_display = ('title', 'fashion_year', 'created_at', 'updated_at')

@admin.register(StyleIcon)
class StyleIconAdmin(admin.ModelAdmin):
    list_display = ('name', 'fashion_year', 'created_at', 'updated_at')