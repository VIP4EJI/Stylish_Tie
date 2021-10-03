$(document).ready(() => {
    // Сценарий валидации данных, вводимых в форму регистрации:
    // ========================================================
    let validateResult1 = false;    // - результат валидации логина
    let validateResult2 = false;     // - результат валидации 1 пароля
    let validateResult3 = false;     // - результат валидации 2 пароля
    let validateResult4 = false;     // - результат валидации e-mail

    // Валидация логина:
    // =================
    $('#login').blur(() => {
        let loginX = $('#login').val();
        let loginRe = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
        if (loginRe.test(loginX)) {
            // Прверка занятости логина:
            $.ajax({
                url: '/accounts/ajax_reg',
                data: 'login=' + loginX,
                success: (result) => {
                    if (result.message === 'занят') {
                        $('#login_err').text('Логин - занят!');
                        validateResult1 = false;
                    } else {
                        validateResult1 = true;
                    }
                }
            });
        } else {
            validateResult1 = false;
            $('#login_err').text('Ошибка формата ввода => от 6 до 16 символов: буквы, цифры, _, -');
        }
    });

    // Валидация 1 пароля:
    // ===================
    $('#pass1').blur(() => {
        let pass1X = $('#pass1').val();
        let passRe = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_\-])[a-zA-Z0-9_\-]{8,}$/;
        if (passRe.test(pass1X)) {
            validateResult2 = true;
            $('#pass1_err').text('');
        } else {
            validateResult2 = false;
            $('#pass1_err').text('Должна быть хотя бы одна буква, хотя бы одна большая буква, хотя бы одна цифра, хотя бы один спецсимвол');
        }
    });

    // Валидация 2 пароля:
    // ===================
    $('#pass2').blur(() => {
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();
        if (pass1X === pass2X) {
            validateResult3 = true;
            $('#pass2_err').text('');
        } else {
            validateResult3 = false;
            $('#pass2_err').text('Пароли не совпадают');
        }
    });

    // Валидация E-Mail:
    // =================
    $('#email').blur(() => {
        let emailX = $('#email').val();
        let emailRe = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailRe.test(emailX)) {
            validateResult4 = true;
            $('#email_err').text('');
        } else {
            validateResult4 = false;
            $('#email_err').text('Стандартная электронная почта: username@host.domain');
        }
    });

    // Итоговая проверка результатов валидации и триггер канала Submit:
    // ================================================================
    $('#submit').click(() => {
        if (
            validateResult1 === true &&
            validateResult2 === true &&
            validateResult3 === true &&
            validateResult4 === true
        ) {
            $('#form-1').attr('onsubmit', 'return true');
        } else {
            $('#form-1').attr('onsubmit', 'return false');
            alert('Форма содержит некорректные данные! \nОтправка данных заблокирована!');
        }
    });

    // Обработка сброса сообщений об ошибках:
    // ======================================
    $('#login').focus(() => {
        // - login
        $('#login_err').text('');
    });

    $('#pass1').focus(() => {
        // - pass1
        $('#pass1_err').text('');
    });

    $('#pass2').focus(() => {
        // - pass2
        $('#pass2_err').text('');
    });

    $('#email').focus(() => {
        // - email
        $('#email_err').text('');
    });
});