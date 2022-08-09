import random
from time import sleep

from utilities.base_page import BasePage
from datetime import datetime, timedelta
from page_locators import deals_page_loc as dpl
from utilities.general import project_path
from static import data
from utilities.custom_logger import customLogger as cl
from utilities.general import get_random_email
import logging


class Deals(BasePage):
    log = cl(logger=logging.getLogger(__name__))

    def click_new_deals(self):
        self.wait_till_element_is_present(dpl.new_deals)
        self.click(dpl.new_deals)
        self.log.info("Clicked 'New Deal' button")

    def select_profile(self, profile):
        self.wait_till_element_is_present(dpl.select_profile_btn)
        self.click(dpl.select_profile_btn)
        sleep(1)
        profile_loc = f"xpath@@//li[text()='{profile}']"
        self.wait_till_element_is_visible(profile_loc)
        self.click(profile_loc)
        self.log.info(f"Selected '{profile}' for the deal")

    def select_deal_type(self, deal_type):
        if deal_type == "Assure Standard":
            self.wait_till_element_is_present(dpl.assure_standard_type)
            self.click(dpl.assure_standard_type)
            self.log.info(f"Selected {deal_type} as deal type")
        if deal_type == "Assure Labs":
            self.wait_till_element_is_present(dpl.assure_labs_type)
            self.click(dpl.assure_labs_type)
            self.log.info(f"Selected {deal_type} as deal type")

    def click_enter_deal_details(self):
        self.wait_till_element_is_present(dpl.enter_deal_details)
        self.click(dpl.enter_deal_details)

    def enter_deal_information(self):
        name = "Test" + datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        target = random.randint(10000, 50000)
        minimum = random.randint(10, 500)
        carry = random.randint(1, 30)
        self.wait_till_element_is_present(dpl.deal_name_field)
        self.send_keys(dpl.deal_name_field, name)
        self.send_keys(dpl.deal_logo_field, project_path.strpath + "/static/logo.png")
        self.send_keys(dpl.deal_desc_field, data.description)
        self.send_keys(dpl.target_amount, target)
        self.send_keys(dpl.mini_invest_amnt, minimum)
        self.send_keys(dpl.carry_percent, carry)
        # self.send_keys(dpl.close_date,(datetime.now()+timedelta(days=10)).strftime("%m%d%yyyy"))
        self.send_keys(dpl.close_date, "01012025")
        self.log.info(f"Enter {name},{target},{minimum},{carry} as name,target value,minimum value,carry")
        self.click(dpl.deal_gen_doc)
        self.log.info("Clicked generate documents")

    def verify_deal_creation_success(self):
        self.wait_till_element_is_present(dpl.deal_suc_alert)
        text_ = self.find_element(dpl.messge).text
        assert self.find_element(dpl.messge).text == "Success", f"Actuall message was {text_}"
        self.click(dpl.ok_btn)
        self.log.info("Verified deal creation success message")

    def upload_my_documents(self):
        self.send_keys(dpl.deal_logo_field, project_path.strpath + "/static/dealer_docs.png")
        sec = 0
        while sec < 60:
            if len(self.find_elements(dpl.downloads_doc)) == 6:
                break
            else:
                sleep(1)
                sec+=1

        self.wait_till_element_is_present(dpl.review_accept)
        self.click(dpl.review_accept)
        self.log.info("Uploaded deal documentation and marked as reviewed")

    def approved_and_cont(self):
        self.click(dpl.approval_btn)
        self.log.info("Deal information Approved and continued\n\n")
        self.wait_till_element_is_present(dpl.skip_step)
        self.click(dpl.skip_step)
        self.log.info("Skipped the invitation part")

    def verify_deal_page(self):
        self.wait_till_url_contains("view-details")
        assert self.driver.current_url
        self.log.info("Redirected to deal details view")

    def open_first_deal(self):
        self.wait_till_element_is_present(dpl.deals)
        self.click(dpl.deals)
        self.wait_till_url_contains("view-details")
        deal_id = self.driver.current_url.split("/")[-1]
        self.log.info(f"Redirect to deal details page with dealID: {deal_id}")

    def edit_carry_percentage(self):
        carry_per = random.randint(1, 30)
        self.click(dpl.carry_sec)
        self.log.info(f"Moved to Carry section")
        sleep(4)
        self.wait_till_element_is_present(dpl.carry_edit_btn).click()
        # self.hover(dpl.carry_edit_btn).click()
        self.move_and_click(dpl.flat_fee_input,3)  # xpath here same as mngmnt flat fee input
        self.click_backspace(dpl.flat_fee_input, 4)
        self.send_keys(dpl.flat_fee_input, carry_per)
        self.click(dpl.mngnt_fee_save_n_cls_btn)
        self.log.info(f"Edited carry percentage as {carry_per}")
        self.wait_till_element_is_invisible(dpl.editor_dialog)

    def edit_management_percentage(self):
        mng_percent = random.randint(1, 7)
        self.click(dpl.mngment_fee_sec)
        self.log.info(f"Moved to Management section")
        sleep(4)
        self.wait_till_element_is_present(dpl.edit_mng_fee_btn).click()
        self.move_and_click("xpath@@//input[@name='percent']",3)
        self.click_backspace(dpl.mngmnt_perc_input, 4)
        self.send_keys(dpl.mngmnt_perc_input, mng_percent)
        self.click(dpl.mngnt_fee_save_n_cls_btn)
        self.wait_till_element_is_invisible(dpl.editor_dialog)
        self.log.info(f"Edited management percentage as {mng_percent}")

    def click_invite_investor(self):
        self.wait_for_page_loaded()
        self.wait_till_element_is_present(dpl.invite_p)
        self.click(dpl.invite_p)
        self.click(dpl.invite_investor)
        self.log.info("Clicked invite investor from deal page")

    def insert_email_and_send_invite(self):
        mails = ''
        for i in range(random.randint(2, 5)):
            mails += get_random_email()+" "
        self.wait_till_element_is_present(dpl.invite_mail_input)
        self.send_keys(dpl.invite_mail_input, mails)
        self.log.info("Entered mails")
        self.click(dpl.sent_invite_btn)
        self.log.info("Send Invite button clicked")
        self.wait_till_element_is_invisible(dpl.sent_invite_btn)

    def verify_invitation_sent_success_message(self):
        self.wait_till_element_is_present(dpl.succes_msg)
        self.log.info("Send invitation success message displayed")
