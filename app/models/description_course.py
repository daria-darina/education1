from django.db import models


class DescriptionCourse(models.Model):
    name = models.CharField(verbose_name='Название курса',max_length=256)
    task = models.CharField(verbose_name='Тема',max_length=50)
    university = models.CharField(verbose_name='Университет', max_length=256)
    duration = models.CharField(verbose_name='Продолжительность', max_length=20)
    date_of_start = models.DateField(verbose_name='Дата начала курса')
    date_of_finish = models.DateField(verbose_name='Дата окончания курса')
    description = models.TextField(verbose_name='Описание курса')
    image = models.ImageField(verbose_name='Изображение')


    class Meta:
        """Meta"""

        verbose_name = 'Описание курса'
        verbose_name_plural = 'Описание курса'