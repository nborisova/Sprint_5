from locators import AuthCheckingLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class TestUserRegistration:

    #Регистрация пользователя
    def test_user_registration_valid_data_account_is_created(self, driver):
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

        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/regiatration' and driver.find_element(*AuthCheckingLocators.USER_AVATAR) and driver.find_element(*AuthCheckingLocators.USER_NAME)

    #Регистрация пользователя с невалидным значением email
    def test_user_registration_invalid_email_error_shown(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*AuthCheckingLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*AuthCheckingLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.SUBMIT_PASSWORD_INPUT))

        email = ''.join(random.choices(string.ascii_lowercase, k=7))

        driver.find_element(*AuthCheckingLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthCheckingLocators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*AuthCheckingLocators.SUBMIT_PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*AuthCheckingLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.ERROR_MESSAGE))

        assert driver.find_element(*AuthCheckingLocators.EMAIL_INPUT_ERR) and driver.find_element(*AuthCheckingLocators.PASSWORD_INPUT_ERR) and driver.find_element(*AuthCheckingLocators.SUBMIT_PASSWORD_INPUT_ERR) and driver.find_element(*AuthCheckingLocators.ERROR_MESSAGE)

    #Регистрация уже существующего пользователя
    def test_user_registration_existing_email_error_shown(self, driver):
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
        driver.find_element(*AuthCheckingLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.SUBMIT_PASSWORD_INPUT))
        driver.find_element(*AuthCheckingLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthCheckingLocators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*AuthCheckingLocators.SUBMIT_PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*AuthCheckingLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthCheckingLocators.ERROR_MESSAGE))

        assert driver.find_element(*AuthCheckingLocators.EMAIL_INPUT_ERR) and driver.find_element(*AuthCheckingLocators.PASSWORD_INPUT_ERR) and driver.find_element(*AuthCheckingLocators.SUBMIT_PASSWORD_INPUT_ERR) and driver.find_element(*AuthCheckingLocators.ERROR_MESSAGE)