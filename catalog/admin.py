from django.contrib import admin

from catalog.models import Category, Product, Contact, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'item_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'ind_number',)
    list_filter = ('name', 'address')
    search_fields = ('name', 'email')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_active')
    list_filter = ('is_active',)
