from locators import AuthCheckingLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class TestUserLogout:
    def test_user_logout_existing_user_success_logout(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*AuthCheckingLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*AuthCheckingLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.SUBMIT_PASSWORD_INPUT))

        email = f"{''.join(random.choices(string.ascii_lowercase, k=7))}@gmail.com"

        driver.find_element(*AuthCheckingLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthCheckingLocators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*AuthCheckingLocators.SUBMIT_PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*AuthCheckingLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.USER_AVATAR))

        driver.find_element(*AuthCheckingLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.LOGIN_AND_REGISTRATION_BUTTON))

        driver.find_element(*AuthCheckingLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*AuthCheckingLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthCheckingLocators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*AuthCheckingLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.USER_AVATAR))
        driver.find_element(*AuthCheckingLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.LOGIN_AND_REGISTRATION_BUTTON))

        assert driver.find_element(*AuthCheckingLocators.LOGIN_AND_REGISTRATION_BUTTON)