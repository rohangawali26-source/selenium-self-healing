from utils.dom import capture_dom
from locator_store.locators import get_locator

def heal_locator(driver, key):
    original = get_locator(key)
    candidates = capture_dom(driver, original["tag"])

    for item in candidates:
        if original["text"] in item["text"]:
            return item["element"]

    raise Exception("Unable to heal locator")
