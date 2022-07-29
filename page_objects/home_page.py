from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
from page_locators import home_page_loc as hml
import logging


class HomePage(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def go_to_homepage(self):
        self.open_homepage()
        self.log.info("\n\nOpened Homepage")
        self.click(hml.cookie_accept)

    def click_login(self):
        self.click(hml.alread_have_an_accnt)

