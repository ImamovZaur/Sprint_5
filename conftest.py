import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import const
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(const.MAIN_URL)
    yield browser
    browser.quit()

@pytest.fixture
def logged_user(driver):
    driver.get(const.LOGIN_PAGE)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.LOGIN_EMAIL_INPUT)))
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(const.EMAIL_FOR_LOGIN)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(const.PASSWORD_FOR_LOGIN)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.PERSONAL_ACCOUNT)))
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    return driver