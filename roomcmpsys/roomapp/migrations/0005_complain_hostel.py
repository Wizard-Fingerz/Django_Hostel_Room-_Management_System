# Generated by Django 4.0.6 on 2022-08-07 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0004_alter_user_complaints_alter_user_hostel'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='hostel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomapp.hostel'),
        ),
    ]
