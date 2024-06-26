# Generated by Django 5.0.3 on 2024-04-06 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Название компании')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имейл')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('ind_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='ИНН')),
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
                ('name', models.CharField(max_length=150, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('item_pic',
                 models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Изображение товара')),
                ('item_price',
                 models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за единицу товара')),
                ('created_date',
                 models.DateField(auto_now_add=True, null=True, verbose_name='Дата внесения товара в базу')),
                ('last_edited_date',
                 models.DateField(auto_now=True, null=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category',
                                               verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ('name', 'item_price'),
            },
        ),
    ]
