from BugBusters.data.constants import Constants


def test_successful_registration(app):
    # Навигация
    app.registration.navigate_to_registration()

    # Регистрация с данными из констант
    app.registration.register(
        name=Constants.USER_NAME,
        email=Constants.EMAIL,
        password=Constants.PASSWORD,
        confirm_password=Constants.PASSWORD
    )

    # Проверка успеха
    assert app.registration.is_registration_successful(), "Account registered"


#def test_registration_with_password_mismatch(app):
#    app.registration.navigate_to_registration()
#
#    # Специально передаем  неактуальным email
#    app.registration.register(
#        name=Constants.USER_NAME,
#        email="newuseregmail.com",
#        password=Constants.PASSWORD,
#        confirm_password=Constants.PASSWORD
#
#    )
#
#    # Проверка появления ошибки
#    error_message = app.registration.get_error_message()
#    assert error_message.is_visible(), "Invalid login or password"