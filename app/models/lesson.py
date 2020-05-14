from django.db import models
from transliterate import translit

def upload_location(instance,filename):
  return "%s/%s" %('video',translit(filename,'ru',reversed=True))

class Lesson(models.Model):
    lecture = models.FileField(upload_to=upload_location,blank=True, null=True, verbose_name='Лекция')
    task = models.CharField(verbose_name='Тема',max_length=50)
    name = models.CharField(verbose_name='Название',max_length=256)
    teacher = models.CharField(verbose_name='ФИО преподавателя',max_length=128)
    homework = models.URLField(verbose_name='Домашнее задание')
    mark = models.PositiveIntegerField(verbose_name='Оценка')
    answer = models.URLField(verbose_name='Домашняя работа')


    class Meta:
        """Meta"""

        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'