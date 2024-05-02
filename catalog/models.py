from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара', **NULLABLE)
    description = models.TextField(verbose_name='Описание товара', **NULLABLE)
    item_pic = models.ImageField(upload_to="catalog/", verbose_name='Изображение товара', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу товара', **NULLABLE)
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата внесения товара в базу', **NULLABLE)
    last_edited_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.item_price} {self.category} '

    class Meta:
        verbose_name = 'товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'товары'  # Настройка для наименования набора объектов
        ordering = ('name', 'item_price')


class Contact(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название компании", **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    email = models.CharField(max_length=200, verbose_name='Имейл', **NULLABLE)
    address = models.TextField(verbose_name='Адрес', **NULLABLE)
    ind_number = models.CharField(max_length=30, verbose_name='ИНН', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name}: {self.phone}, {self.email}, {self.address}, {self.ind_number}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(default=1, verbose_name='Номер')
    name = models.CharField(max_length=100, default='Создана', verbose_name='Название')
    is_active = models.BooleanField(default=True, verbose_name='Активная')

    def __str__(self):
        return f'{self.name} {self.number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'