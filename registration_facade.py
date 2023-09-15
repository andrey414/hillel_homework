from selenium_work.facad.base_facade import BaseFacade


class RegistrationFacade(BaseFacade):
    def __init__(self,driver):
        super().__init__(driver)

    def register_user(self,name,last_name,email,password,repeat_password):
        self.main_page.sign_up_button().click()
        self.registration_form_page.name_field().send_keys(name)
        self.registration_form_page.last_name_field().send_keys(last_name)
        self.registration_form_page.email_field().send_keys(email)
        self.registration_form_page.password_field().send_keys(password)
        self.registration_form_page.reenter_password_field().send_keys(repeat_password)
        self.registration_form_page.register_button().click()

    def check_is_user_login(self):
        return len(self.garage_page.empty_garage()) > 0
