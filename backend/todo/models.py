from django.db import models


class Todo(models.Model):
    name = models.CharField('Наименование', max_length=255)
    date_add = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата изменения', auto_now=True)
    is_done = models.BooleanField('Выполнено', default=False)

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Списки дел'

    def __str__(self):
        return self.name
