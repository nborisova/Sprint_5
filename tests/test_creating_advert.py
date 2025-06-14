from locators import AuthCheckingLocators
from locators import AdvertCheckingLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class TestCreatingAdvert:
    #Попытка разместить объявление неавторизованным пользователем
    def test_creating_advert_unauthorized_user_authorization_is_required(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')

        driver.find_element(*AdvertCheckingLocators.PLACE_ADVERT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AdvertCheckingLocators.PLACE_ADVERT_BUTTON))

        assert driver.find_element(*AdvertCheckingLocators.UNAUTHORIZED_USER_HEADER_IN_ADV_FORM).text == 'Чтобы разместить объявление, авторизуйтесь'

    #Размещение объявления авторизованным пользователем
    def test_creating_advert_authorized_user_new_advert_is_displayed(self, driver):
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

        driver.find_element(*AdvertCheckingLocators.PLACE_ADVERT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AdvertCheckingLocators.PLACE_ADVERT_BUTTON))

        advert_name = ''.join(random.choices(string.ascii_lowercase, k=7))

        driver.find_element(*AdvertCheckingLocators.NAME_INPUT).click()
        driver.find_element(*AdvertCheckingLocators.NAME_INPUT).send_keys(advert_name)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CATEGORY_DROPDOWN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CATEGORY_ITEM)).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CONDITION_RADIO_BUTTON)).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CITY_DROPDOWN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CITY_ITEM)).click()

        element = driver.find_element(*AdvertCheckingLocators.DESCRIPTION_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        element.send_keys('TestAdv0 Description')

        driver.find_element(*AdvertCheckingLocators.PRICE_INPUT).click()
        driver.find_element(*AdvertCheckingLocators.PRICE_INPUT).send_keys('989')
        
        driver.find_element(*AdvertCheckingLocators.PUBLISH_BUTTON).click()

        #Поиск добавленной карточки
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AdvertCheckingLocators.CARD))
        driver.find_element(*AdvertCheckingLocators.SEARCH_TEXT_INPUT).click()
        driver.find_element(*AdvertCheckingLocators.SEARCH_TEXT_INPUT).send_keys(advert_name)
        driver.find_element(*AdvertCheckingLocators.CATEGORY_DROPDOWN).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CATEGORY_ITEM)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CITY_DROPDOWN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AdvertCheckingLocators.CITY_ITEM)).click()
        driver.find_element(*AdvertCheckingLocators.SEARCH_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdvertCheckingLocators.NEW_AD_CARD_NAME))

        assert driver.find_element(*AdvertCheckingLocators.NEW_AD_CARD_NAME).text == advert_name
