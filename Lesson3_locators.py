from selenium.webdriver.common.by import By


    #Links
    INTERNAL_LINK = (By.CSS_SELECTOR, "a[href*='/teams']")
    CREATE_ACCOUNT_HEADER = (By.XPATH, "//h1[text()='Create your account']")
    DISCLAIMER_CONTAINER = (By.CSS_SELECTOR, "div.js-terms")

    #Forms
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")

    #Buttons
    SIGN_UP_BUTTON = (By.ID, "submit-button")
    GOOGLE_SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[data-provider='google']")
    GITHUB_SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[data-provider='github']")