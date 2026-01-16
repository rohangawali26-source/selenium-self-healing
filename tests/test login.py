def test_login(driver):
    driver.get("https://example.com")
    login = find_element(driver, "login_button")
    login.click()
