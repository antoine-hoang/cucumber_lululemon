from behave import *
from selenium import webdriver
from features.page_object.booking_page import BookingPage
from features.page_object.login_page import LoginPage


@given('the user has logged in successfully - Room number scenario')
def log_in_positive(context):
    context.driver = webdriver.Chrome()
    login_page = LoginPage(context.driver)
    login_page.open()
    login_page.execute_login("admin", "password")
    booking_page = BookingPage(context.driver)
    assert booking_page.is_logout_button_displayed()


@when('the user creates its two rooms - Room number scenario')
def create_rooms_negative_room_number(context):
    booking_page = BookingPage(context.driver)
    booking_page.create_room("234", "Family", "true", "600", 1, 1, 1, 1, 1, 1)
    booking_page.clear_room_details()
    booking_page.create_room("", "Suite", "false", "950", 1, 0, 0, 1, 1, 0)


@then('the application indicates an error - Room number scenario')
def error_message_room_number(context):
    booking_page = BookingPage(context.driver)
    assert booking_page.is_room_name_error_displayed()


@then('close the browser - unsuccessful room creation - Room number scenario')
def closeBrowser(context):
    context.driver.close()
