# Generated by Django 5.0.1 on 2024-11-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
