from django.db import models



class Student(models.Model):
    name = models.CharField("ФИО", max_length=255)
    year = models.CharField("Год поступления", max_length=4)
    faculty = models.TextField("Факультет")
    direction = models.CharField("Группа", max_length=10)
    email = models.EmailField("Email")
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"
    

class Task(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField("Наименование задания", max_length=255)
    text = models.TextField("Решение")
    grade = models.CharField("Оценка", max_length=1)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return f"{self.name} - {self.student.name} - {self.grade}"
