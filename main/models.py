from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255,verbose_name='Имя')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    unikID = models.TextField(verbose_name='Уникальный ID')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время отправки')
    subscription = models.TextField(default="null",verbose_name='Абонемент')
    activity = models.BooleanField(default=False,verbose_name='Активность')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-time_create', 'unikID']

        def __str__(self):
            return self.name
