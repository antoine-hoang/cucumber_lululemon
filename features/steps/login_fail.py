from behave import *
from selenium import webdriver
from features.page_object.login_page import LoginPage


@given('the user has incorrect credentials')
def wrong_cred(context):
    context.driver = webdriver.Chrome()
    login_page = LoginPage(context.driver)
    login_page.open()


@when('the user tries to log in')
def wrong_login(context):
    login_page = LoginPage(context.driver)
    login_page.execute_login("administrator", "password123")


@then('the application indicates an error')
def error_indicator(context):
    login_page = LoginPage(context.driver)
    assert login_page.check_wrong_credentials()


@then('close the browser - unsuccessful login')
def closeBrowser(context):
    context.driver.close()
