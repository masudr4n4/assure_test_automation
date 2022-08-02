from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
import logging



class ProfileOrg(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def click_create_new_org_profile(self):
        pass