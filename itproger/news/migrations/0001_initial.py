# Generated by Django 5.1.2 on 2024-10-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='unknown', max_length=50, verbose_name='Название')),
                ('anons', models.CharField(default='unknown', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(default='unknown', verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
