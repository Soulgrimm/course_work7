# Generated by Django 5.0.6 on 2024-05-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_habit_next_send_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='next_send_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата следующей отправки'),
        ),
    ]
