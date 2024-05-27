# Generated by Django 5.0.6 on 2024-05-25 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('sign_pl_habit', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('periodicity', models.SmallIntegerField(default=1, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='вознаграждение')),
                ('complete_time', models.DurationField(blank=True, null=True, verbose_name='время на выполнение')),
                ('sign_publication', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связанная привычка')),
                ('is_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
