from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


# ===== LOCATORS =====
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
EMPTY_CART_MSG = (By.XPATH, "//h1[contains(text(), 'empty')]")

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='shippingButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[href="/cart"]')

PRODUCT_NAME = (By.CSS_SELECTOR, 'div[data-test="cartItem-title"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-title']")
CART_ITEMS = (By.CSS_SELECTOR, '[data-test="cart-rail-summary"] div[class="h-padding-r-tight"] h2 span')


# ===== GIVEN =====
@given("Open Target main page")
def open_target(context):
    context.driver.get("https://www.target.com/")
    sleep(3)


# ===== WHEN =====
@when("Click on cart icon")
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(2)


@when("Search for mug")
def search_mug(context):
    search_box = context.driver.find_element(By.NAME, "searchTerm")
    search_box.send_keys("mug")
    search_box.submit()
    sleep(3)


@when("Click on product")
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/p/']").click()
    sleep(3)


@when("Click on Add to Cart button")
def click_add_to_cart(context):
    sleep(5)  # wait for banner to disappear
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(3)


@when("Store product name")
def store_product_name(context):
    context.product = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print("Saved product:", context.product)


@when("Confirm Add to Cart button from side navigation")
def confirm_add_to_cart(context):
    sleep(3)
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(3)


@when("Open cart page")
def open_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


# ===== THEN =====
@then("Empty Cart message is shown")
def verify_empty_cart(context):
    message = context.driver.find_element(*EMPTY_CART_MSG)
    assert message.is_displayed(), "Empty cart message not shown"


@then("Verify cart has 1 item(s)")
def verify_cart(context):
    items = context.driver.find_element(*CART_ITEMS).text
    assert '1 item' in items, f"Expected 1 item, got {items}"


@then("Verify product in cart is correct")
def verify_product(context):
    actual = context.driver.find_element(*PRODUCT_NAME).text
    expected = context.product
    assert actual == expected, f'Expected:"{expected}", but got: "{actual}"'