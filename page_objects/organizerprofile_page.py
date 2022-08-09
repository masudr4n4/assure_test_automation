from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
import logging
from page_locators import profile_page_loc as ppl
from static import data


class ProfileOrg(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def click_create_new_org_profile(self):
        self.wait_till_element_is_present(ppl.new_profiles_btn)
        self.click(ppl.new_profiles_btn)
        self.click(ppl.new_org_profile)

    def choose_new_profile_type_as(self, type):
        if type == 'Individual':
            self.click(ppl.create_individual_btn)
        else:
            raise ValueError("No profile type chosen")

    def enter_auth_tax_info(self):
        self.send_keys(ppl.auth_tax_res_fname, data.auth_tax_rep_fname)
        self.send_keys(ppl.auth_tax_res_lname, data.auth_tax_rep_lname)
        self.send_keys(ppl.auth_tax_res_add1, data.auth_tax_address)
        self.send_keys(ppl.auth_tax_res_add2, data.auth_tax_address)
        self.send_keys(ppl.auth_tax_dob, data.dob)
        self.send_keys(ppl.auth_tax_res_city, "Mobile")
        self.click(ppl.auth_tax_res_state)
        self.send_keys(ppl.auth_tax_res_state, "Alabama")
        self.click(ppl.ala)
        self.send_keys(ppl.auth_tax_res_ssn,data.auth_tax_ssn)

    def click_create_profile(self):
        self.move_and_click(ppl.create_individual_profile_btn)

    def delete_profile(self, profile_type):
        raise NotImplemented("Not Implemented yet")

