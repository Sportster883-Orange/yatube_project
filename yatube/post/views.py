# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страницо')


def group_posts(request, slug):
    return HttpResponse('Список постоф')
