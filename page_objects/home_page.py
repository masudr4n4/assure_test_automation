from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
from page_locators import home_page_loc as hml
import logging


class HomePage(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def go_to_homepage(self):
        self.open_homepage()
        self.log.info("\n\nOpened Homepage")
        try:
            self.click(hml.cookie_accept)
        except:
            pass
        self.driver.execute_script('window.localStorage["li_ignored"] =[{"id":3312863,"time":1659427299784}]')

    def click_login(self):
        self.click(hml.alread_have_an_accnt)

    def go_to_profiles(self):
        self.click(hml.setting_icon)
        self.wait_till_element_is_present(hml.profile_sec)
        self.click(hml.profile_sec)
        self.log.info("Moved to profiles section")


