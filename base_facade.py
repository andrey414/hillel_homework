from selenium_work.page.garage_page import GaragePage
from selenium_work.page.main_page import MainPage
from selenium_work.page.registration_form_page import RegistrationFormPage


class BaseFacade:
    def __init__(self,driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.registration_form_page = RegistrationFormPage(self.driver)
        self.garage_page = GaragePage(self.driver)

