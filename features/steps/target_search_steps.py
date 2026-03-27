from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Locator for Target's search input field using data-test attribute
SEARCH_INPUT = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')


@given("Open Target homepage")
def open_target(context):
    # Open the Target website
    context.driver.get("https://www.target.com/")


@when('Search Target for "{item}"')
def search_target(context, item):
    search = context.driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search.clear()
    search.send_keys(item)
    search.send_keys(Keys.ENTER)


@then('Target search results contain "{item}"')
def verify_results(context, item):
    # Verify the search results page contains the search term in the URL
    assert item.lower() in context.driver.current_url.lower(), \
        f'Expected "{item}" in URL, got: {context.driver.current_url}'

    # Pause briefly so the results page can be seen before the browser closes
    time.sleep(3)