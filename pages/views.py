from django.shortcuts import render

def home_view(request):
    # Словник data - це і є наш КОНТЕКСТ
    data = {
        'title': 'Моя Лаба 3',
        'header_text': 'Вітаю на головній сторінці!',
        'description': 'Цей текст був змінений за допомогою рендера та контекста.'
    }
    return render(request, 'pages/index.html', data)

def about_view(request):
    return render(request, 'pages/about.html')