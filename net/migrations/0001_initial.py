# Generated by Django 5.0.1 on 2024-01-15 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('organization_type', models.CharField(choices=[('factory', 'factory'), ('net', 'net'), ('entrepreneur', 'entrepreneur')], max_length=100, verbose_name='тип организации')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='задолженность')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='net.organization', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street_name', models.CharField(max_length=100, verbose_name='улица')),
                ('number', models.CharField(max_length=5, verbose_name='номер дома')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.organization', verbose_name='организация')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название продукта')),
                ('model', models.CharField(max_length=100, verbose_name='модель продукта')),
                ('launch_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.organization', verbose_name='организация')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]