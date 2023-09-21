from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    first_name = models.CharField(max_length=50, verbose_name='имя')
    middle_name = models.CharField(max_length=50, **NULLABLE, verbose_name='отчество')
    email = models.EmailField(unique=True, verbose_name='почта')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'Ф.И.О: {self.last_name} {self.first_name} {self.middle_name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
