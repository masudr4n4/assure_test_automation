from behave import *
from page_objects.deals_page import Deals

@step('I click on "{invite}" to invite investor for the deal')
def step_impl(context,invite):
    """
    :type context: behave.runner.Context
    """
    Deals(context).click_invite_investor()


@then("I insert email addresses and Click Send invite")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).insert_email_and_send_invite()


@step("I verify invitation sent success message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).verify_invitation_sent_success_message()