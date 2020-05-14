from django.db import models
from django.conf import settings
from .lesson import Lesson
from .description_course import DescriptionCourse
from django.contrib.auth.models import User


class Course(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description_course = models.ForeignKey(DescriptionCourse, verbose_name = 'Описание курса', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name='Урок', on_delete=models.CASCADE)
    test = models.URLField(verbose_name='Тест')
    mark = models.PositiveIntegerField(verbose_name='Итоговый балл')
    sertificate = models.BooleanField(verbose_name='Наличие сертификата', default=False)




    class Meta:
        """Meta"""

        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'