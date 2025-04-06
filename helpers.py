from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker


def wait_for_element_located(driver, locator, time, condition):
    return WebDriverWait(driver, time).until(condition(locator))


def fake_email():
    fake = Faker()
    return fake.email()