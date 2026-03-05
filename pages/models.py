from django.db import models


# 1. Головна таблиця: Епоха / Рік
class FashionYear(models.Model):
    year = models.IntegerField(verbose_name="Рік (напр. 1990)", unique=True)
    description = models.TextField(verbose_name="Опис епохи")

    # Вимога: Створено о, Оновлено о
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Епоха моди"
        verbose_name_plural = "Епохи моди"


# 2. Таблиця: Тренд (Об'єднана з FashionYear)
class Trend(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва тренду")
    # Вимога: Обов'язково об'єднати хоча б дві таблиці (робимо через ForeignKey)
    fashion_year = models.ForeignKey(FashionYear, on_delete=models.CASCADE, verbose_name="Рік")
    details = models.TextField(verbose_name="Опис тренду")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тренд"
        verbose_name_plural = "Тренди"


# 3. Таблиця: Ікона стилю (Об'єднана з FashionYear)
class StyleIcon(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ім'я людини")
    fashion_year = models.ForeignKey(FashionYear, on_delete=models.CASCADE, verbose_name="Рік")
    outfit = models.TextField(verbose_name="Що одягнуто")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ікона стилю"
        verbose_name_plural = "Ікони стилю"