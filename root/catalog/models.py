from django.db import models
from django.urls import reverse


# 1 - Модель категории товара:
# ============================
class Category(models.Model):
    # Свойства модели:
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')  # Строковое поле с индексацией
    slug = models.SlugField(max_length=100, unique=True, null=True, verbose_name='Ссылка')  # уникальные URL-адреса title

    # Метаданные
    class Meta:
        ordering = ('title',)  # Сортировка/кортеж
        verbose_name = 'Категория'  # Имя в единственном числе
        verbose_name_plural = 'Категории'  # Имя в множественном числе

    # Метод __str__() - представление обьекта, читаемое по умолчанию
    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self):
        return reverse('index', args=[self.slug])


# 2 - Модель производителя товара:
# ================================
class Producer(models.Model):
    # Свойства модели:
    title = models.CharField(max_length=100, db_index=True)

    # Метод __str__() - представление обьекта, читаемое по умолчанию
    def __str__(self) -> str:
        return str(self.title)


# 3 - Модель самого товара:
# =========================
class Product(models.Model):
    # Свойства модели:
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=100, db_index=True, null=True, verbose_name='Ссылка')
    about = models.TextField(max_length=500, db_index=True, verbose_name='Описание')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)  # внешний ключ производителя
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # внешний ключ категории
    picture = models.FileField(upload_to='pictures/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')  # лучше точность округления чем Float
    available = models.BooleanField(default=True, verbose_name='Наличие')
    count = models.IntegerField(verbose_name='Количество')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    # Метаданные
    class Meta:
        ordering = ('title',)  # Сортировка/кортеж
        verbose_name = 'Товар'  # Имя в единственном числе
        verbose_name_plural = 'Товары'  # Имя в множественном числе
        index_together = (('id', 'slug'), )  # кортеж полей проиндексирован вместе

    # Метод __str__() - представление обьекта, читаемое по умолчанию
    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self):
        return reverse('details', args=[self.slug])
