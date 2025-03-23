from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators
from const import LOGIN_PAGE

class TestStellarBurgers:
    def test_logout_button(self, driver, logged_user):
        conftest.wait_for_element_located(driver, time=7, locator=Locators.FOOTER_TEXT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        conftest.wait_for_element_located(driver, time=7, locator=Locators.LOGIN_BUTTON, condition=EC.presence_of_element_located)
        assert LOGIN_PAGE == driver.current_url