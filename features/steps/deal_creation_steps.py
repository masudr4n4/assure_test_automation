from behave import *
from page_objects.deals_page import Deals


@then('I select "{profile}" as organizer profile')
def step_impl(context, profile):
    """
    :type context: behave.runner.Context
    """
    Deals(context).select_profile(profile)


@step('I select "{deal_type}" as the deal type')
def step_impl(context,deal_type):
    """
    :type context: behave.runner.Context
    """
    Deals(context).select_deal_type(deal_type)


@step('I click "Enter deal details" in the first step')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).click_enter_deal_details()


@then("I enter new deal information and generate documents")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).enter_deal_information()


@step("I verify Deal creation success message and dismiss it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).verify_deal_creation_success()


@step("I upload my deal documents and accept as reviewed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).upload_my_documents()


@then("I Approved and continue and skip the invitation step")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).approved_and_cont()


@step("I verify the created deal page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).verify_deal_page()

