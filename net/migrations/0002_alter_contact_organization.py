# Generated by Django 5.0.1 on 2024-01-15 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='net.organization', verbose_name='организация'),
        ),
    ]