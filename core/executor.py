from selenium.webdriver.common.by import By
from core.healer import heal_locator
from locator_store.locators import get_locator

def find_element(driver, key):
    locator = get_locator(key)

    try:
        return driver.find_element(By.XPATH, locator["xpath"])
    except Exception:
        return heal_locator(driver, key)
