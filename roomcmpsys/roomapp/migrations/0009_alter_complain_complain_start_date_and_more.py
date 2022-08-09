# Generated by Django 4.0.6 on 2022-08-09 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0008_remove_user_complaints_complain_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='complain_start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='complain',
            name='date_reported',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
