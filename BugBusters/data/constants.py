import os
from dotenv import load_dotenv

# 1. Сначала загружаем переменные из .env
load_dotenv()

class Constants:
    # 2. Теперь присваиваем значения
    BASE_URL = "https://stg.polakohedonist.club/en"
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    USER_NAME = os.getenv("USER_NAME")
    TIMEOUT = 5000