from django.db import models

class Table(models.Model):
    name = models.CharField("ФИО", max_length=255)
    year = models.CharField("Год поступления", max_length=4)
    faculty = models.TextField("Факультет")
    direction = models.TextField("Направление подготовки")
    email = models.EmailField("Email")
    
    class Meta:
        verbose_name = "Таблица"
        verbose_name_plural = "Таблицы"

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"