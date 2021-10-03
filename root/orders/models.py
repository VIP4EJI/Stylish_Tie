from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='E-mail', null=True)
    address = models.CharField(max_length=250, verbose_name='Адрес', null=True)
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс', null=True)
    city = models.CharField(max_length=100, verbose_name='Город', null=True)
    amount = models.IntegerField(verbose_name='Количество')
    date = models.DateTimeField(null=False, default=timezone.now)
    status = models.CharField(max_length=100, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Созданый')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    paid = models.BooleanField(default=False, verbose_name='Оплаченый')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
