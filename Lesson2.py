from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open Amazon Sign-In page
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
sleep(8)

# Amazon logo - search by XPath using aria-label
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email field - search by ID
driver.find_element(By.ID, "ap_email_login")

# Continue button - search by ID
driver.find_element(By.ID, "continue")

# Conditions of Use link - search by XPath using text
driver.find_element(By.XPATH, "//a[contains(text(),'Conditions of Use')]")

# Privacy Notice link - search by XPath using text
driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Notice')]")

# Need help link - search by XPath using text
driver.find_element(By.XPATH, "//a[contains(text(),'Need help')]")

# Forgot your password link (appears on password page) - search by ID
# driver.find_element(By.ID, "auth-fpp-link-bottom")

# Other issues with Sign-In link (not shown in my Amazon flow) - expected locator
# driver.find_element(By.XPATH, "//a[contains(text(),'Other issues with Sign-In')]")

# Create a free business account button (shown instead of create account) - search by XPath using text
driver.find_element(By.XPATH, "//span[contains(text(),'Create a free business account')]")

sleep(3)
driver.quit()
