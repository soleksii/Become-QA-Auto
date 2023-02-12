import pytest
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_wrong_login():
    # Створення об'єкту сторінки
    signInPage = SignInPage()

    # Відкриваємо сторінку Github
    signInPage.go_to()

    # Виконуємо спробу увійти в систему Github
    signInPage.try_login('tester', 'password')

    # Перевіряємо що назва сторінки така, яку ми очікуємо
    assert signInPage.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    signInPage.close()
