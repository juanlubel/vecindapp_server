# Generated by Django 3.0.4 on 2020-04-01 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20200401_1712'),
        ('profiles', '0006_propietario_apartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquilino',
            name='apartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Apartment'),
        ),
    ]
