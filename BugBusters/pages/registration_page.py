import re
from BugBusters.pages.base_page import BasePage
from BugBusters.data.constants import Constants


class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Ищем кнопку входа (Sign In)
        self.login_btn = page.locator("a, button").get_by_text("Sign In")
        # Ищем ссылку на регистрацию
        self.no_account_link = page.get_by_text("Don't have an account", exact=False)

    def navigate_to_registration(self):
        self.login_btn.first.wait_for(state="visible", timeout=10000)
        self.login_btn.first.click()
        self.no_account_link.wait_for(state="visible", timeout=10000)
        self.no_account_link.click()

    def fill_registration_form(self, name, email, password, confirm_password):
        # ВАЖНО: Мы убрали "#Name" и используем get_by_placeholder
        # Это сработает, так как в поле написано слово Name
        name_input = self.page.get_by_placeholder("Name")
        name_input.wait_for(state="visible", timeout=10000)
        name_input.fill(name)

        self.page.get_by_placeholder("Email").fill(email)

        # Пароли
        pass_fields = self.page.get_by_placeholder(re.compile(r"Password", re.IGNORECASE))
        pass_fields.first.fill(password)
        pass_fields.last.fill(confirm_password)

    def submit_registration(self):
        # Исправлено: Sign Up
        self.page.get_by_role("button", name=re.compile("Sign Up", re.IGNORECASE)).click()

    def register(self, name, email, password, confirm_password):
        # Передаем все 4 аргумента
        self.fill_registration_form(name, email, password, confirm_password)
        self.submit_registration()

    def is_registration_successful(self):
        # Используем текст из констант (или просто строку, если константа не задана)
        success_text = "Account registered"

        # Создаем локатор для текста
        success_locator = self.page.get_by_text(success_text)

        try:
            # Ждем появления элемента на странице до 5000 мс (5 секунд)
            success_locator.wait_for(state="visible", timeout=5000)
            return True
        except:
            # Если через 5 секунд текст не появился - возвращаем False
            return False

    def get_error_message(self):
        return self.page.locator(".error-message")