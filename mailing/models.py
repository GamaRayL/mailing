from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    frequency_choices = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )

    status_choices = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('closed', 'Завершена'),
    )

    send_time = models.DateTimeField(verbose_name='время рассылки')
    frequency = models.CharField(max_length=10, choices=frequency_choices, verbose_name='периодичность')
    status = models.CharField(max_length=10, choices=status_choices, verbose_name='статус')

    def __str__(self):
        return f'{self.get_frequency_display()} рассылка в {self.send_time}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    title = models.CharField(max_length=255, verbose_name='тема')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Log(models.Model):
    status_choices = (
        ('success', 'Успешно'),
        ('failure', 'Неуспешно'),
    )

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    status = models.CharField(max_length=10, choices=status_choices, verbose_name='статус')
    attempt_datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    server_response = models.TextField(**NULLABLE, verbose_name='ответ от сервера')

    def __str__(self):
        return f'{self.mailing} - {self.status} ({self.attempt_datetime})'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
