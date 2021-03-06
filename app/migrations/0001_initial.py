# Generated by Django 3.0.6 on 2020-05-11 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название курса')),
                ('task', models.CharField(max_length=50, verbose_name='Тема')),
                ('university', models.CharField(max_length=256, verbose_name='Университет')),
                ('duration', models.CharField(max_length=20, verbose_name='Продолжительность')),
                ('date_of_start', models.DateField(verbose_name='Дата начала курса')),
                ('date_of_finish', models.DateField(verbose_name='Дата окончания курса')),
                ('description', models.TextField(verbose_name='Описание курса')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Описание курса',
                'verbose_name_plural': 'Описание курса',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.URLField(verbose_name='Лекция')),
                ('task', models.CharField(max_length=50, verbose_name='Тема')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('teacher', models.CharField(max_length=128, verbose_name='ФИО преподавателя')),
                ('homework', models.URLField(verbose_name='Домашнее задание')),
                ('mark', models.PositiveIntegerField(verbose_name='Оценка')),
                ('answer', models.URLField(verbose_name='Домашняя работа')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.URLField(verbose_name='Тест')),
                ('mark', models.PositiveIntegerField(verbose_name='Итоговый балл')),
                ('sertificate', models.BooleanField(default=False, verbose_name='Наличие сертификата')),
                ('description_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DescriptionCourse', verbose_name='Описание курса')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Lesson', verbose_name='Урок')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
