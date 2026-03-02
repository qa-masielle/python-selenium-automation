from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given("I open target.com")
def open_target(context):
    context.driver.get("https://www.target.com/")

@when("I click on the cart icon")
def click_cart(context):
    cart = context.driver.find_element(By.CSS_SELECTOR, "a[href*='/cart']")
    cart.click()

@then('I should see "Your cart is empty"')
def verify_empty_cart(context):
    time.sleep(2)
    assert "Your cart is empty" in context.driver.page_source