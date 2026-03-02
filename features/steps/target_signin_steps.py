from behave import when, then
from selenium.webdriver.common.by import By
import time

@when("I click Sign In")
def step_click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()

@when("from the side menu I click Sign In")
def step_click_sign_in_side_menu(context):
    pass

@then("I should see the Sign In form")
def step_verify_sign_in_form(context):
    pass