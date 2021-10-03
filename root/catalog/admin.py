from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Producer, Product


#  Декораторы на реестрацию
#  Доваление моделей и настройка отображения их на сайте админки
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']  # Заголовок
    prepopulated_fields = {'slug': ('title',)}  # При вводе нового заголовка slug заполняется автоматически


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'picture_show', 'price', 'available', 'uploaded']
    list_filter = ['available', 'uploaded']  # атрибут позволяющий фильтровать результаты по полям/правая боковая панель
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}

    def picture_show(self, obj):
        if obj.picture:
            return mark_safe("<img src='{}' width='60' />".format(obj.picture.url))
        return "None"

    picture_show.__name__ = "Картинка"

