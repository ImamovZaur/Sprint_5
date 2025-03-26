from selenium.webdriver.support import expected_conditions as EC

import const
from data import *
from locators import Locators
from helpers import *

class TestStellarBurgers:

    def test_registration_new_user(self, driver):
        wait_for_element_located(driver, time=3, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        wait_for_element_located(driver, time=3, locator=Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(email+password)
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        wait_for_element_located(driver,time=5, locator=Locators.LOGIN_BUTTON, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait_for_element_located(driver, time=10, locator=Locators.PERSONAL_ACCOUNT, condition=EC.element_to_be_clickable)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert wait_for_element_located(driver, time=15, locator=Locators.FOOTER_TEXT, condition=EC.visibility_of_element_located)



    def test_registration_invalid_password(self, driver):
        wait_for_element_located(driver, time=3, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        wait_for_element_located(driver, time=3, locator=Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(const.NAME_FOR_REGISTRATION)
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(const.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys('12345')
        wait_for_element_located(driver, time=3, locator=Locators.REGISTRATION_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert wait_for_element_located(driver, time=17, locator=Locators.ERROR_MESSAGE, condition=EC.visibility_of_element_located)