from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username: str, password: str) -> None:
        """Sign in to GitHub
        :param username: set username or email
        :param password: set password
        """

        # Find the field in which we will enter the wrong username or postal address
        login_element = self.driver.find_element(By.ID, "login_field")

        # Enter username or email address
        login_element.send_keys(username)

        # Find the field in which we will enter the wrong password
        password_element = self.driver.find_element(By.ID, "password")

        # Enter the wrong password
        password_element.send_keys(password)

        # Find the "Sign in" button
        button_element = self.driver.find_element(By.NAME, "commit")

        # Emulate a click of the left mouse button
        button_element.click()

    def check_title(self, expected_title: str) -> bool:
        """Check title
        :param expected_title: set title
        """

        return self.driver.title == expected_title
