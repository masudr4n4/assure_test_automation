from time import sleep

from static import data
from utilities.base_page import BasePage
from utilities.custom_logger import customLogger as cl
from page_locators import inv_profile_page_loc as ppc
from utilities.general import get_random_email
import logging


class InvestorProfile(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def click_new_profile(self):
        self.wait_till_element_is_present(ppc.new_profile_btn)
        self.wait_till_element_is_visible(ppc.new_profile_btn)
        self.move_and_click(ppc.new_profile_btn, 3)

    def enter_similar_input_for_profile(self, city, state, add1=None, add2=None, postal_code=None, ):
        self.wait_for_page_loaded()
        if add1:
            self.send_keys(add1, data.address)
        else:
            self.send_keys(ppc.address_1, data.address)

        if add2:
            self.send_keys(add2, data.address)
        else:
            self.send_keys(ppc.address_2, data.address)
        if postal_code:
            self.move_and_click(postal_code)
            self.send_keys(postal_code, "36617")
        else:
            self.move_and_click(ppc.postal_code)
            self.send_keys(ppc.postal_code, '36617')
        self.send_keys(city, "Mobile")
        self.click(state)
        self.find_element(state).send_keys("Alabama")
        self.find_element(ppc.ala).click()

    def us_citizen(self, us):
        self.click(us)
        self.click(ppc.ssn_input)
        self.move_and_send_keys(ppc.ssn_input, data.ssn_id)

    def not_us_citzen(self):
        self.click(ppc.not_us_btn)
        self.click("xpath@@//input[@name='countryOfFormation']")
        self.click("xpath@@//li[text()='Bangladesh']")
        self.send_keys("xpath@@//input[@name='id1']",'6532458712')
        self.click("xpath@@//input[@name='documentType']")
        raise NotImplemented("Fix no us ")

    def fill_out_information_for_individual_account(self, us=True):
        self.wait_till_element_is_present(ppc.loaded_mail, 5)
        self.enter_similar_input_for_profile(ppc.city, ppc.state)
        self.send_keys(ppc.date_of_birth, "01012000")
        if us:
            self.us_citizen(ppc.us_yes)
        else:
            self.not_us_citzen()

    def submit_profile_info(self):
        self.click(ppc.create_individual)
        self.wait_till_element_is_invisible(ppc.create_individual)

    def check_mark_investor_accreditation(self):
        self.wait_till_element_is_present(ppc.investor_accreditation_btn)
        self.move_and_click(ppc.investor_accreditation_btn)
        self.move_and_click(ppc.accreditation_option1)
        self.move_and_click(ppc.accreditation_option2)

    def click_create_profile(self):
        self.wait_till_element_is_present(ppc.create_profile, 5)
        self.move_and_click(ppc.create_profile)
        self.wait_till_element_is_invisible(ppc.create_profile)

    def delete_new_created_profile(self, profile_type=None):
        if profile_type == 'individual':
            self.wait_till_element_is_present(ppc.invdividual_profile_dlt_btn)
            self.click(ppc.invdividual_profile_dlt_btn)
            self.wait_till_element_is_present(ppc.delete_success_pop, 7)
        elif profile_type == "entity":
            self.wait_till_element_is_present(ppc.delete_btn_for_entity)
            self.move_and_click(ppc.delete_btn_for_entity)
        elif profile_type == "trust":
            self.wait_till_element_is_present(ppc.delete_btn_for_trust)
            self.move_and_click(ppc.delete_btn_for_trust)
        elif profile_type == 'joint':
            self.wait_till_element_is_present(ppc.joint_profile_dlt_btn)
            self.move_and_click(ppc.joint_profile_dlt_btn)
        elif profile_type == 'retire':
            self.wait_till_element_is_present(ppc.retirement_profile_dlt_btn)
            self.move_and_click(ppc.retirement_profile_dlt_btn)
        else:
            raise ValueError("No profile type found")
        self.wait_till_element_is_present(ppc.delete_success_pop)
        delet_succ_msg = self.find_element(ppc.delete_success_pop).text
        assert "Success" in delet_succ_msg, "Profile delete message don't have success message"
        assert "deleted" in delet_succ_msg, "Profile delete message not showed"
        self.click(ppc.close_dialog)
        self.log.info("Click close button for delete dialog box")

    def add_f_n_lname(self):
        self.send_keys(ppc.first_name, data.first_name)
        self.send_keys(ppc.last_name, data.last_name)

    def add_signatory(self):
        self.click(ppc.add_signatory_btn)
        self.wait_till_element_is_visible(ppc.add_signatory_txt, 6)
        self.enter_similar_input_for_profile(ppc.sign_city_input, ppc.sign_state_input, add1=ppc.signatory_add1,
                                             add2=ppc.signatory_add2, postal_code=ppc.signatory_postal_code)
        self.send_keys(ppc.date_of_birth, "01012001")
        self.click(ppc.sig_us_cit_yes)
        self.send_keys(ppc.ssn_input, data.ssn_id)
        self.add_f_n_lname()
        self.send_keys(ppc.signatory_title, "developer")
        self.move_and_click(ppc.save_signatory_btn)

    def select_account_type_for_entity_account(self,type):
        self.move_and_click(ppc.entity_type_selecion)
        if type == "LP":
            self.wait_till_element_is_clickable(ppc.LIMITED_PARTNER,3)
            self.click(ppc.LIMITED_PARTNER)
        else:
            raise ValueError("No profile type selected")


    def select_entity_profile_section(self):
        self.move_and_click(ppc.entity_profile_sec)
        self.wait_till_element_is_present(ppc.entiy_profile_selected, 4)
        self.wait_till_element_is_present(ppc.loaded_mail)

    def fill_out_information_for_entity_account(self):
        self.send_keys(ppc.entity_name_input, data.entity_name)
        self.enter_similar_input_for_profile(ppc.city, ppc.state, add1=ppc.address_1, add2=ppc.address_2,
                                             postal_code=ppc.postal_code)
        self.send_keys(ppc.ein_input, data.ein_id)
        self.add_signatory()
        self.move_and_click(ppc.save_cre_entity_p_btn)
        self.wait_till_element_is_invisible(ppc.save_cre_entity_p_btn)

    def check_mark_entity_accreditation(self):
        self.wait_till_element_is_present(ppc.entity_accr)
        self.click(ppc.entity_accr)
        self.move_and_click(ppc.accreditation_option1)
        self.move_and_click(ppc.accreditation_option2)

    def click_create_profile_ent(self):
        self.move_and_click(ppc.create_profile_ent)
        self.wait_till_element_is_invisible(ppc.create_profile_ent)

    def fill_out_information_for_trust_account(self):
        self.log.info("Started entering trust account information")
        self.move_and_click(ppc.trust_p_sec)
        self.wait_till_element_is_present(ppc.trust_p_selected, 4)
        self.send_keys(ppc.ein_input, data.ein_id)
        self.send_keys(ppc.trust_name, data.trust_account_name)
        self.enter_similar_input_for_profile(ppc.city, ppc.state)
        self.send_keys(ppc.signer_title, data.title)
        self.send_keys(ppc.date_of_birth, data.dob)
        self.us_citizen(ppc.signer_us)
        self.send_keys(ppc.first_name, data.first_name)
        self.send_keys(ppc.last_name, data.last_name)
        self.move_and_click(ppc.submit_trust_p)
        self.log.info("Entered and clicked submit button for trust account")

    def mark_trust_accredditation(self):
        self.wait_till_element_is_present(ppc.trust_accre)
        self.click(ppc.trust_accre)
        self.move_and_click(ppc.accreditation_option1)
        self.move_and_click(ppc.accreditation_option2)
        self.log.info("Checked the trust accreditation and clicked create profile")

    def add_signatory_fn_ln_em(self):
        email = get_random_email()
        self.wait_till_element_is_present(ppc.signatory_fname)
        self.move_and_click(ppc.signatory_fname)
        self.move_and_send_keys(ppc.signatory_fname, data.first_name)
        self.move_and_click(ppc.signatory_lname)
        self.move_and_send_keys(ppc.signatory_lname, data.last_name)
        self.move_and_click(ppc.signatory_email)
        self.move_and_send_keys(ppc.signatory_email, email)
        self.log.info(f"Entered fname,lname and the email is :{email} for the signatory")
        self.move_and_click(ppc.signatory_joint_save_btn)
        self.wait_till_element_is_invisible(ppc.signatory_joint_save_btn)

    def fill_out_information_for_joint_account(self):
        self.move_and_click(ppc.joint_p_sec)
        self.wait_till_element_is_present(ppc.joint_p_selected)
        self.log.info("Moved to joint profile section")
        self.send_keys(ppc.joint_d_name, data.display_name)
        self.send_keys(ppc.trust_name, data.joint_account_name)  # xpath is same as trust name
        self.send_keys(ppc.first_name, data.first_name)
        self.send_keys(ppc.last_name, data.last_name)
        self.send_keys(ppc.date_of_birth, data.dob)
        self.send_keys(ppc.signer_title, data.title)
        self.enter_similar_input_for_profile(ppc.city, ppc.state)
        self.us_citizen(ppc.joint_signer_us)
        self.move_and_click(ppc.add_joint_signatory_btn, 2)
        self.add_signatory_fn_ln_em()
        self.move_and_click(ppc.joint_accre_btn)
        self.log.info("Entered joint profile information and click joint accreditation")

    def mark_joint_accreditation(self):
        self.wait_till_element_is_present(ppc.joint_accre_op)
        self.move_and_click(ppc.joint_accre_op)
        self.move_and_click(ppc.accreditation_option1)
        self.move_and_click(ppc.accreditation_option2)
        self.log.info("Checked the trust accreditation and clicked create profile")

    def check_retirement_investor_accreditation(self):
        self.wait_till_element_is_present(ppc.retire_acreditation)
        self.click(ppc.retire_acreditation)
        self.move_and_click(ppc.accreditation_option1)
        self.move_and_click(ppc.accreditation_option2)
        self.log.info("Checked the retirement investor accreditation and clicked create profile")

    def fill_out_information_for_retirement_account(self):
        self.move_and_click(ppc.retirement_sec)
        self.wait_till_element_is_present(ppc.retirement_sec_selected)
        self.wait_till_element_is_present(ppc.loaded_mail)
        self.us_citizen(ppc.retire_us_city)
        self.enter_similar_input_for_profile(ppc.city, ppc.state)
        self.send_keys(ppc.date_of_birth, data.dob)
        self.move_and_click(ppc.IRA)
        self.move_and_click(ppc.submit_retire_profile)
        self.wait_till_element_is_present(ppc.retirement_next_btn)
        self.click(ppc.retirement_next_btn)
        self.log.info("Click next button on the extra dialog box for retirement")

    def create_profile_retirement(self):
        self.move_and_click(ppc.create_profile)
        self.log.info("Entered Retirement profile information and clicked Create profile")

    def delete_all_profile(self):
        # self.wait_for_page_loaded(10)
        try:
            self.wait_till_element_is_present(ppc.profiles_dlt_btn,6)
        except:
            pass
        while True:
            if len(self.find_elements(ppc.profiles_dlt_btn)) > 0:
                self.wait_till_element_is_present(ppc.profiles_dlt_btn,4)
                self.click(ppc.profiles_dlt_btn)
                self.wait_till_element_is_present(ppc.close_dialog,4)
                self.click(ppc.close_dialog)
            else:
                break