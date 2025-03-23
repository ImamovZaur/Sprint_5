from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators

class TestStellarBurgers:
    def test_button_bread(self, driver):
        conftest.wait_for_element_located (driver, time=5, locator=Locators.SAUCE_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        conftest.wait_for_element_located(driver, time=5, locator=Locators.BULKI_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.BULKI_BUTTON).click()
        assert driver.find_element(*Locators.BULKI_BUTTON).text == 'Булки'


    def test_button_sauces(self, driver):
        conftest.wait_for_element_located(driver, time=5, locator=Locators.FILLING_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.FILLING_BUTTON).click()
        conftest.wait_for_element_located(driver, time=5, locator=Locators.SAUCE_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        assert driver.find_element(*Locators.SAUCE_BUTTON).text == 'Соусы'

    def test_button_filling(self, driver):
        conftest.wait_for_element_located(driver, time=5, locator=Locators.FILLING_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.FILLING_BUTTON).click()
        assert driver.find_element(*Locators.FILLING_BUTTON).text == 'Начинки'