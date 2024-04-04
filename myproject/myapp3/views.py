from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


def hello(request):
    return HttpResponse('Hello world from function!!!')


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello world from class!!!')
    
def year_post(request, year):
    text = ''
    ... # Формируем статьи за год
    return HttpResponse(f'Posts from {year}<br>{text}')



class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        ... # Формируем статьи за год и месяц
        return HttpResponse(f'Posts from {month}/{year}<br>{text}')
    
def post_detail(request, year, month, slug):
    ... # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})

    
    
# Create your views here.
