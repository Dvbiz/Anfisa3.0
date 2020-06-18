from django.http import HttpResponse
from django.shortcuts import render
from . import anfisa


def about(request):
    return render(request, 'templates/about.html')


def index(request):
    html = ''
    if request.method == 'POST':
        # извлекаем из POST-запроса вопрос пользователя
        query = request.POST['query']

        # допишите ваш код здесь
        answer = anfisa.process_query(query)

        # полученный из anfisa.py ответ оборачиваем в HTML-теги, будет нарядно
        html = f'<p class = "askMe__request">{answer}</p>'

    # подготовьте словарь context, чтобы вывести информацию в шаблон
    context = {
        'response': html,  # сюда передайте HTML-код с ответом Анфисы
        'where': request.path  # передаём абсолютный адрес страницы
    }

    # добавьте словарь context третьим аргументом
    return render(request, 'templates/index.html', context)
def new_friend(request):
    html = ''
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        answer = anfisa.new_friend(name, city)
        html = f'<p class ="content__answer">{answer} <a class="question__link" href="/">Задать вопрос?</a></p>'
    context = {
        'response': html, 
        'where': request.path
    }
    return render(request, 'templates/new-friend.html', context)