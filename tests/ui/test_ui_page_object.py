import pytest
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_wrong_login():
    # Create page object
    signInPage = SignInPage()

    # Open the "Github" page
    signInPage.go_to()

    # Trying to login to the Github
    signInPage.try_login('tester', 'password')

    # Check if the page name is expected
    assert signInPage.check_title("Sign in to GitHub · GitHub")

    # Close the browser
    signInPage.close()
