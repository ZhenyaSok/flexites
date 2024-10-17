from django.db import models


NULLABLE = {"null": True, "blank": True}

class Company(models.Model):
    """ Модель организации"""
    title = models.CharField(max_length=150, verbose_name='Название организации')
    description = models.TextField(verbose_name='Краткое описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
