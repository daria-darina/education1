from django.db import models
from transliterate import translit
from app.models import Course
from embed_video.fields import EmbedVideoField

def upload_location(instance,filename):
  return "%s/%s" %('video',translit(filename,'ru',reversed=True))

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='Урок', on_delete=models.CASCADE, null=True)
    video = EmbedVideoField(blank=True, verbose_name='Видео')
    task = models.CharField(verbose_name='Тема',max_length=50)
    name = models.CharField(verbose_name='Название',max_length=256)
    teacher = models.CharField(verbose_name='ФИО преподавателя',max_length=128)
    homework = models.URLField(verbose_name='Домашнее задание')
    mark = models.PositiveIntegerField(verbose_name='Оценка')
    answer = models.FileField(verbose_name='Домашняя работа', upload_to='media/', null=True)


    class Meta:
        """Meta"""

        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'