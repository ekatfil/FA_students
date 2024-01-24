from django.shortcuts import render, redirect
from .models import *
import json
from django.http import HttpResponseForbidden, JsonResponse

def index(request):

    content = {
        "title": "Главная",
    }

    return render(request, "main/index.html", content)


def table(request):
    table = Table.objects.all()

    content = {
        "title": "Таблица",
        "tables": table,
    }

    return render(request, "main/table.html", content)


def add_table(request):
    if request.method == "POST":
        name = request.POST.get('name')
        year = request.POST.get('year')
        faculty = request.POST.get('faculty')
        direction = request.POST.get('direction')
        email = request.POST.get('email')
        id = request.POST.get('id')

        if id:
            table = Table.objects.get(pk=id)
            table.name = name
            table.year = year
            table.faculty = faculty
            table.direction = direction
            table.email = email
            table.save()
        else:
            # Если запись новая, создаем новый объект
            table = Table.objects.create(
                name=name,
                year=year,
                faculty=faculty,
                direction=direction,
                email=email
            )

        # return JsonResponse({"created": "success"}, status=200)
            
        return redirect('table')

    return JsonResponse({"error": "Invalid request method"}, status=400)

def about(request):

    content = {
        "title": "О проекте",
    }

    return render(request, "main/about.html", content)