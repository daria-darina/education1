# Generated by Django 3.0.6 on 2020-05-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200515_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='answer',
            field=models.FileField(null=True, upload_to='media/', verbose_name='Домашняя работа'),
        ),
    ]