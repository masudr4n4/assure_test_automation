from behave import *
from page_objects.signup_page import SignUp



@step("I fill out sign up information for creating new account and submit")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.email = SignUp(context).fill_out_sign_up_info()


@then("I agree with term and conditions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    SignUp(context).accept_agreements()


@given("I on a deal invitation page on sign up purpose")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    SignUp(context).open_deal_invitation_page()


@step("I fill out sign up information for creating new account and submit with invited email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.email = SignUp(context).fill_out_sign_up_info(email=context.email)