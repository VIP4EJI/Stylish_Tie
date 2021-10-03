from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from catalog.models import Product
from .models import Cart
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart/detail.html', context={
        'user_cart': Cart.objects.filter(user_id=request.user.id)
    })


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart/detail.html', context={
        'user_cart': Cart.objects.filter(user_id=request.user.id)
    })


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def index(request):
    return render(request, 'orders/index.html', context={
        'title': 'Список заказов',
        'user_carts': Cart.objects.filter(user_id=request.user.id)
    })


def confirm(request):
    return render(request, 'orders/confirm.html', context={
        'title': 'Подтверждение заказа',
        'user_carts': Cart.objects.filter(user_id=request.user.id)
    })


def ajax_basket(request):
    # 1 - Извлекаем параметры заказа из AJAX-запроса:
    response = dict()
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    price = request.GET.get('price')

    # 2 - Создаем новый заказ и сохраняем его в БД:
    Cart.objects.create(
        title=f'Cart-{pid}/{uid}',
        amount=float(price),
        status='ожидание подтверждения',
        product_id=pid,
        user_id=uid
    )

    # 3 - Извлекаем список всех заказов данного пользователя:
    user_carts = Cart.objects.filter(user_id=uid)

    # 4 - Вычисляем общую стоимость всех покупок данного пользователя:
    s = 0
    for cart in user_carts:
        s += cart.amount

    # 5 - Записываем в ответ общую стоимость и количество товаров:
    response['amount'] = s
    response['count'] = len(user_carts)

    # 6 - Отправляем ответ в JS:
    return JsonResponse(response)


def ajax_basket_display(request):
    # 1 - Создаем пустой словарь для сборки отчета на AJAX-запроса:
    response = dict()

    # 2 - Извлекаем ID-пользователя из AJAX-запроса:
    uid = request.GET['uid']

    # 3 - Извлекаем список всех заказов данного пользователя:
    user_carts = Cart.objects.filter(user_id=uid)

    # 4 - Вычисляем общую стоимость всех покупок данного пользователя:
    s = 0
    for cart in user_carts:
        s += cart.amount

    # 5 - Записываем в ответ общую стоимость и количество товаров:
    response['amount'] = s
    response['count'] = len(user_carts)

    # 6 - Отправляем ответ в JS:
    return JsonResponse(response)

