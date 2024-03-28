from django.db import models


# Create your models here.
""""
    Абстрактная модель, предоставляющая поля для отслеживания даты создания
    и последнего изменения объекта.
    """
class Category(models.Model):
    """
    Модель категории товаров.
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    ordering = ('title',)

    def __str__(self):
        return f'{self.title}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    Модель продукта.
    """
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(
        verbose_name='описание', blank=True, null=True)
    preview = models.ImageField(
        upload_to='products/',
        verbose_name='изображение',
        blank=True,
        null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
        blank=True,
        null=True)
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания')
    changed = models.DateTimeField(
        auto_now=True,
        verbose_name='дата последнего изменения')
    price = models.IntegerField(verbose_name='цена за покупку')

    def __str__(self):
        return f'{self.title}: {self.description} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
