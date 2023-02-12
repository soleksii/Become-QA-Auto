from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
        login_element = self.driver.find_element(By.ID, "login_field")

        # Вводимо ім'я користувача або поштову адресу
        login_element.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        password_element = self.driver.find_element(By.ID, "password")

        # Вводимо неправильний пароль
        password_element.send_keys(password)

        # Знаходимо кнопку sign in
        button_element = self.driver.find_element(By.NAME, "commit")

        # Емулюємо клік лівої кнопки миші
        button_element.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
