# Generated by Django 5.0.6 on 2024-05-28 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_alter_habit_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'ordering': ('pk',), 'verbose_name': 'привычка', 'verbose_name_plural': 'привычки'},
        ),
    ]
