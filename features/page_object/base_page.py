from selenium.common import NoSuchElementException, InvalidElementStateException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_clickable(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _select_from_dropdown(self, locator: tuple, choice: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        Select(WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable(locator))).select_by_value(choice)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _get_style(self, locator: tuple, time: int = 10) -> str:
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(ec.text_to_be_present_in_element_attribute(locator, "style", "border: 1px solid red;"))
            return self._find(locator).get_attribute("style")
        except TimeoutException:
            pass

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _is_selected(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_selected()
        except InvalidElementStateException:
            return False
