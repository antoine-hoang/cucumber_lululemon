import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from features.page_object.base_page import BasePage


class BookingPage(BasePage):
    __create_button = (By.ID, "createRoom")
    __room_number = (By.ID, "roomName")
    __room_type = (By.ID, "type")
    __room_accessible = (By.ID, "accessible")
    __room_price = (By.ID, "roomPrice")
    __room_details_wifi = (By.ID, "wifiCheckbox")
    __room_details_tv = (By.ID, "tvCheckbox")
    __room_details_radio = (By.ID, "radioCheckbox")
    __room_details_refreshments = (By.ID, "refreshCheckbox")
    __room_details_safe = (By.ID, "safeCheckbox")
    __room_details_views = (By.ID, "viewsCheckbox")
    __bookings_list = (By.XPATH, "//div[@data-testid='roomlisting']")
    __log_out_button_locator = (By.XPATH, "//div[@id='root']//nav/div[3]/ul//a[@href='#/admin']")
    __room_name_error = (By.XPATH, "/html//div[@id='root']/div[2]/div[@class='container']//div[@class='alert alert-danger']/p[.='Room name must be set']")
    __room_price_error = (By.XPATH, "/html//div[@id='root']/div[2]/div[@class='container']//div[@class='alert alert-danger']/p[.='must be greater than or equal to 1']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def create_room(self, room_number: str, room_type: str, room_accessible: str, room_price: str, room_details_wifi: int, room_details_tv: int, room_details_radio: int, room_details_refreshments: int, room_details_safe: int, room_details_views: int):
        super()._type(self.__room_number, room_number)
        super()._select_from_dropdown(self.__room_type, room_type)
        super()._select_from_dropdown(self.__room_accessible, room_accessible)
        super()._type(self.__room_price, room_price)
        if room_details_wifi == 1:
            super()._click(self.__room_details_wifi)
        if room_details_tv == 1:
            super()._click(self.__room_details_tv)
        if room_details_radio == 1:
            super()._click(self.__room_details_radio)
        if room_details_refreshments == 1:
            super()._click(self.__room_details_refreshments)
        if room_details_safe == 1:
            super()._click(self.__room_details_safe)
        if room_details_views == 1:
            super()._click(self.__room_details_views)
        super()._click(self.__create_button)
        time.sleep(2)

    def is_logout_button_displayed(self) -> bool:
        time.sleep(2)
        return super()._is_displayed(self.__log_out_button_locator)

    def is_room_name_error_displayed(self) -> bool:
        time.sleep(2)
        return super()._is_displayed(self.__room_name_error)

    def is_room_price_error_displayed(self) -> bool:
        time.sleep(2)
        return super()._is_displayed(self.__room_price_error)

    def clear_room_details(self):
        if super()._is_selected(self.__room_details_wifi):
            super()._click(self.__room_details_wifi)
        if super()._is_selected(self.__room_details_tv):
            super()._click(self.__room_details_tv)
        if super()._is_selected(self.__room_details_radio):
            super()._click(self.__room_details_radio)
        if super()._is_selected(self.__room_details_refreshments):
            super()._click(self.__room_details_refreshments)
        if super()._is_selected(self.__room_details_safe):
            super()._click(self.__room_details_safe)
        if super()._is_selected(self.__room_details_views):
            super()._click(self.__room_details_views)

    def clear_room_form(self):
        super()._find(self.__room_number).clear()
        super()._find(self.__room_price).clear()

    def get_bookings_list(self) -> str:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@data-testid='roomlisting']")))
        booking_list = self._driver.find_elements(By.XPATH, "//div[@data-testid='roomlisting']")
        return booking_list

