
from static import data
from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
from utilities.general import get_random_email_for_org
from page_locators import admin_page_loc as apl
import logging


class Admin(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def logged_in_admin(self):
        self.open(data.admin_url)
        self.wait_for_page_loaded()
        self.wait_till_element_is_present(apl.username_input)
        self.send_keys(apl.username_input,data.admin_username)
        self.send_keys(apl.password_input,data.admin_password)
        self.click(apl.sign_in)
        self.log.info("Logged in to the admin page")

    def send_invitation_for_org(self):
        email = get_random_email_for_org()
        self.wait_till_element_is_present(apl.email_input,10)
        self.send_keys(apl.email_input, email)
        self.click(apl.select_deal_type)
        self.click(apl.standard_deal)
        self.click(apl.add_client)
        self.log.info(f"Sent invitation to {email}")
        return email
