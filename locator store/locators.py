import json
import os

LOCATOR_FILE = os.path.join(
    os.path.dirname(__file__),
    "locators.json"
)

def load_locators():
    with open(LOCATOR_FILE, "r") as f:
        return json.load(f)

def save_locators(data):
    with open(LOCATOR_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_locator(key):
    data = load_locators()
    if key not in data:
        raise KeyError(f"Locator not found: {key}")
    return data[key]

def update_locator(key, new_xpath):
    data = load_locators()

    if key in data:
        data[key]["xpath"] = new_xpath
        save_locators(data)
