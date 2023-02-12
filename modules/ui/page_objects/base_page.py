from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from definition import PROJECT_ROOT


class BasePage:
    DRIVER_NAME = "chromedriver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(PROJECT_ROOT / BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
