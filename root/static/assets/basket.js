$(document).ready(() => {

    $('.add-to-cart').click((event) => {
        // 1 - Определение параметров заказа:
        const user_id = $('#user_id').val();
        if (user_id === 'None') {
            alert('Для использования корзины Вы должны авторизоваться!');
            window.location = '/accounts/sign_in';
        } else {
            let uid = user_id;
            let pid = $(event.target).prev().val();
            let price = $(event.target).parent().prev().find('span').text()

            // 2 - Отправка AJAX-запроса на добавление заказа в БД:
            $.ajax({
                url: '/cart/ajax_basket',
                data: `uid=${uid}&pid=${pid}&price=${price}`,
                success: (result) => {
                    // Отображение изменений в иконке корзины:
                    alert('товар успешно добавлен в корзину! ');
                    let count = result.count;
                    let amount = result.amount;
                    $('#count').text(`Количество товаров: ${count} шт`);
                    $('#amount').text(`Общая стоимость: ${amount} грн`);
                    $('#_count').text(count);
                }
            });
        }
    });

});