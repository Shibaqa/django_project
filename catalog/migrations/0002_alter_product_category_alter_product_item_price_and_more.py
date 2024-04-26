# Generated by Django 5.0.3 on 2024-04-23 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True,
                                      verbose_name='Цена за единицу товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование товара'),
        ),
    ]
