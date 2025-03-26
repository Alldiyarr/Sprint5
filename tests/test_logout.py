from locators import Locators

def test_logout(driver):
    driver.get("https://stellarburgers.nomoreparties.site/account")
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
