from django.shortcuts import render, redirect
from .models import *

def index(request):

    content = {
        "title": "Главная",
    }

    return render(request, "main/index.html", content)


def table(request):

    content = {
        "title": "Таблица",
    }

    return render(request, "main/table.html", content)


def about(request):

    content = {
        "title": "О проекте",
    }

    return render(request, "main/about.html", content)