import os
from dotenv import load_dotenv
from BugBusters.data.constants import Constants

# Загружаем переменные (можно оставить вне функции)
load_dotenv(dotenv_path='.env')


def test_check_environment_variables():
    """Тест для проверки загрузки переменных окружения"""
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    # Вместо print используем assert, чтобы pytest зафиксировал успех
    assert email is not None, "EMAIL не загружен из .env"
    assert password is not None, "PASSWORD не загружен из .env"

    print(f"\nЛогин: {email}")  # Увидишь в консоли при запуске с флагом -s


def test_constants_loading():
    """Тест для проверки связи с классом Constants"""
    assert Constants.EMAIL == os.getenv("EMAIL"), "Email в Constants не совпадает с .env"
    assert Constants.PASSWORD == os.getenv("PASSWORD"), "Password в Constants не совпадает с .env"