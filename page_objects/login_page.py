from time import sleep

from static import data
from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
import logging
from page_locators import login_page_loc as lpl


class LoginPage(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def enter_email_pwd(self, email, password=data.password):
        self.wait_till_element_is_present(lpl.username_field)
        self.send_keys(lpl.username_field, email)
        if password != "empty":
            self.send_keys(lpl.pwd_field, password)
        self.log.info(f"Entered email and password as :{email},{password}")

    def click_login(self):
        self.click(lpl.sign_in)
        self.log.info("clicked sign in")
        self.driver.execute_script('window.localStorage["li_ignored"] =[{"id":3312863,"time":1659427299784}]')

    def verify_user_logged_in(self):
        self.wait_till_url_contains("deals-view",20)
        self.wait_till_element_is_present(lpl.settings_icon, 10)
        assert "deals-view" in self.driver.current_url, f"Current url {self.driver.current_url} expected to have 'deals-view'"

    def verify_user_not_logged_in(self):
        self.wait_till_element_is_present(lpl.warning_msg)
        assert "Invalid" in self.find_element(lpl.warning_msg).text
        self.log.info("Verified user not logged in.")

    def verify_user_logged_in_as_investor(self):
        self.wait_till_url_contains("investment",50)
        assert "investment" in self.driver.current_url,f"Current url {self.driver.current_url} expected to have 'investment'"
        self.log.info("User logged in investor page")

    def verify_login_page(self):
        self.wait_for_page_loaded()
        self.wait_till_element_is_present(lpl.login_header)
        sign_in_text = self.find_element(lpl.h1).get_attribute('value')
        assert sign_in_text == "Sign In", f"Actual text was {sign_in_text}"

    def verify_organizer_welcome_page(self):
        self.wait_till_url_contains("welcome-to-glassboard", 20)
        assert "welcome-to-glassboard" in self.driver.current_url, f"Current url {self.driver.current_url} expected to have 'welcome-to-glassboard'"
        self.log.info("New organizer landed on the welcome page ")

