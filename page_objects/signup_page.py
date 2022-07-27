from time import sleep

from selenium.webdriver.support.select import Select

from utilities.base_page import BasePage
from utilities.general import config
from page_locators import signup_page_loc as spl
from utilities.custom_logger import customLogger as cl
from static import data
import random
import string
import logging

class SignUp(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def open_deal_invitation_page(self):
        base_url = config.get("URL", 'url')
        if "stag" in base_url:
            invitation = data.staging_deal_invitation
        url = base_url + invitation
        self.open(url)
        self.log.info(f"Open a deal invitation base wit : {url}")
        self.wait_till_element_is_present(spl.cookie_con, 10)
        self.click(spl.cookie_con)

    def fill_out_sign_up_info(self):
        s = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
        email = "rana" + s + "@assure.com"
        self.wait_till_element_is_present(spl.f_name)
        self.send_keys(spl.f_name, "Rana")
        self.send_keys(spl.l_name, "Test"+s)
        self.log.info(f"Entered {email},{s} as email and last name")
        self.send_keys(spl.email, email)
        self.send_keys(spl.p_code, "67303")
        select = Select(self.find_element(spl.phon_dr))
        select.select_by_value("BD")
        self.send_keys(spl.tel, "1530124155")
        self.send_keys(spl.dob, "01012001")
        self.click(spl.state)
        self.send_keys(spl.state, "Alabama")
        self.click(spl.alabama)
        self.send_keys(spl.pwd, data.password)
        self.click(spl.submit)
        self.log.info("Clicked submit button for sign up")
        return email

    def accept_agreements(self):
        sleep(3)
        self.wait_till_element_is_present(spl.agree)
        self.click(spl.agree)
        self.log.info("Accepted the sign up agreements")