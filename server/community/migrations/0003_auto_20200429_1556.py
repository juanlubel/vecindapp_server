# Generated by Django 3.0.4 on 2020-04-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20200429_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='piso',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='puerta',
            field=models.CharField(max_length=5),
        ),
    ]
