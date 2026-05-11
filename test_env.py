import os
from dotenv import load_dotenv
from BugBusters.data.constants import Constants

load_dotenv(dotenv_path='.env')


def test_check_environment_variables():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    assert email is not None, "EMAIL не загружен из .env"
    assert password is not None, "PASSWORD не загружен из .env"

    print(f"\nЛогин: {email}")


def test_constants_loading():
    assert Constants.EMAIL == os.getenv("EMAIL"), "Email в Constants не совпадает с .env"
    assert Constants.PASSWORD == os.getenv("PASSWORD"), "Password в Constants не совпадает с .env"