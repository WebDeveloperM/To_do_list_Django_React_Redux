# Generated by Django 4.1.2 on 2023-01-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='index',
            field=models.IntegerField(null=True),
        ),
    ]
