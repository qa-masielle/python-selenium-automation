from behave import given, then
from selenium.webdriver.common.by import By
import time

@given("Open Target Circle page")
def open_target(context):
    # Open the Target circle page
    context.driver.get("https://www.target.com/circle")

@then('Verify there are 2 story cards')
def verify_results(context):
    # Find all story cards on the page
    cards = context.driver.find_elements(By.CSS_SELECTOR,'[data-test="@web/SlingshotComponents/common/Storycard"]')

    #Verify there are exactly 2 cards
    assert len(cards) == 2, f"Expected 2 cards, found {len(cards)}"

    # Pause briefly so the results page can be seen before the browser closes
    time.sleep(3)