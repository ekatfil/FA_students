from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import json
from django.http import HttpResponseForbidden, JsonResponse

def index(request):

    content = {
        "title": "Главная",
    }

    return render(request, "main/index.html", content)


def table(request):
    student = Student.objects.all()

    content = {
        "title": "Таблица студентов",
        "students": student,
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
            student = Student.objects.get(pk=id)
            student.name = name
            student.year = year
            student.faculty = faculty
            student.direction = direction
            student.email = email
            student.save()
        else:
            # Если запись новая, создаем новый объект
            student = Student.objects.create(
                name=name,
                year=year,
                faculty=faculty,
                direction=direction,
                email=email
            )

        # return JsonResponse({"created": "success"}, status=200)
            
        return redirect('table')

    return JsonResponse({"error": "Invalid request method"}, status=400)


def edit_table(request, table_id):
    table = get_object_or_404(Student, id=table_id)

    if request.method == "POST":
        # Обработка данных для редактирования
        name = request.POST.get('name')
        year = request.POST.get('year')
        faculty = request.POST.get('faculty')
        direction = request.POST.get('direction')
        email = request.POST.get('email')

        table.name = name
        table.year = year
        table.faculty = faculty
        table.direction = direction
        table.email = email
        table.save()

        return JsonResponse({"updated": "success"}, status=200)

    # Отображение формы для редактирования
    return render(request, 'edit_table.html', {'table': table})


def delete_table(request, table_id):
    table = get_object_or_404(Student, id=table_id)
    

    if request.method == "POST":
        # Удаление записи
        table.delete()
        # return JsonResponse({"deleted": "success"}, status=200)
        return redirect('table')


def student_detail(request, student_id):

    student = get_object_or_404(Student, id=student_id)
    tasks = Task.objects.filter(student=student)

    content = {
        "student": student,
        "tasks": tasks,
    }

    return render(request, 'main/student_detail.html', content)
    


def about(request):

    content = {
        "title": "О проекте",
    }

    return render(request, "main/about.html", content)