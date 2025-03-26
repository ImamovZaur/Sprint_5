from selenium.webdriver.support import expected_conditions as EC

from helpers import *
from locators import Locators
from const import PROFILE_CABINET

class TestStellarBurgers:
    def test_login(self, driver, logged_user):
        wait_for_element_located(driver, time=17, locator=Locators.PERSONAL_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        wait_for_element_located(driver, time=17, locator=Locators.FOOTER_TEXT, condition=EC.presence_of_element_located)
        assert PROFILE_CABINET == driver.current_url