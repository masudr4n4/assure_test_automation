from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
import logging
from page_locators import login_page_loc as lpl


class LoginPage(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def enter_email_pwd(self, email=None, password=None):
        self.wait_till_element_is_present(lpl.username_field)
        self.send_keys(lpl.username_field,email)
        self.send_keys(lpl.pwd_field,password)
        self.log.info(f"sent email and password as :{email},{password}")

    def click_login(self):
        self.click(lpl.sign_in)
        self.log.info("clicked sign in")

    def verify_user_logged_in(self):
        # self.wait_for_page_loaded()
        self.wait_till_url_contains("deals-view",20)
        self.wait_till_element_is_present(lpl.settings_icon, 10)
        assert "deals-view" in self.driver.current_url,f"Current url {self.driver.current_url} expected to have 'deals-view'"

    def verify_user_not_logged_in(self):
        self.wait_till_element_is_present(lpl.warning_msg)
        assert "Invalid" in self.find_element(lpl.warning_msg).text
        pass
