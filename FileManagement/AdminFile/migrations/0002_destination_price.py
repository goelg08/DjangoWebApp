# Generated by Django 2.0.4 on 2020-03-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminFile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
