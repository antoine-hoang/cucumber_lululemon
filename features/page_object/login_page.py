from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from features.page_object.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://automationintesting.online/#/admin"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __login_button = (By.ID, "doLogin")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__login_button)

    def check_wrong_credentials(self) -> bool:
        error_style = super()._get_style(self.__username_field)
        if error_style == "border: 1px solid red;":
            return True
        else:
            return False

