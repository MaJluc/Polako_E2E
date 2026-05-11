from BugBusters.data.constants import Constants


def test_successful_registration(app):
    app.registration.navigate_to_registration()

    app.registration.register(
        name=Constants.USER_NAME,
        email=Constants.EMAIL,
        password=Constants.PASSWORD,
        confirm_password=Constants.PASSWORD
    )

    assert app.registration.is_registration_successful(), "Account registered"