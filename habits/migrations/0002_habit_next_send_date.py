# Generated by Django 5.0.6 on 2024-05-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='next_send_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата следующего действия'),
        ),
    ]