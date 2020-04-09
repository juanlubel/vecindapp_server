# Generated by Django 3.0.4 on 2020-04-02 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_remove_servicio_community'),
        ('community', '0011_auto_20200402_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='president',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='president', to='profiles.Propietario'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='comunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartaments', to='community.Community'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='renter',
            field=models.ManyToManyField(blank=True, related_name='renter', to='profiles.Inquilino'),
        ),
        migrations.AlterField(
            model_name='community',
            name='instalaciones',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
