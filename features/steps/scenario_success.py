from behave import *
from selenium import webdriver
from features.page_object.booking_page import BookingPage
from features.page_object.login_page import LoginPage


@given('the user has logged in successfully')
def log_in_positive(context):
    context.driver = webdriver.Chrome()
    login_page = LoginPage(context.driver)
    login_page.open()
    login_page.execute_login("admin", "password")
    booking_page = BookingPage(context.driver)
    assert booking_page.is_logout_button_displayed()


@when('the user creates its two rooms')
def create_rooms_positive(context):
    booking_page = BookingPage(context.driver)
    booking_list_start = len(booking_page.get_bookings_list())
    booking_page.create_room("234", "Family", "true", "600", 1, 1, 1, 1, 1, 1)
    booking_page.clear_room_details()
    booking_page.create_room("235", "Suite", "false", "950", 1, 0, 0, 1, 1, 0)
    booking_list_end = len(booking_page.get_bookings_list())
    assert booking_list_end > booking_list_start


@then('the booking list shows the newly created rooms')
def enter_credentials(context):
    booking_page = BookingPage(context.driver)
    booking_list = booking_page.get_bookings_list()
    assert "235" in booking_list[-1].text
    assert "234" in booking_list[-2].text


@then('close the browser - success')
def closeBrowser(context):
    context.driver.close()
