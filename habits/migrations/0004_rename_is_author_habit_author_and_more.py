# Generated by Django 5.0.6 on 2024-05-28 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_next_send_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='is_author',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='habit',
            name='associated_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='периодичность'),
        ),
    ]
