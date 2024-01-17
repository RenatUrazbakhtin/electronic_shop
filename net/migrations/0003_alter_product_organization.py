# Generated by Django 5.0.1 on 2024-01-15 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0002_alter_contact_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='net.organization', verbose_name='организация'),
        ),
    ]