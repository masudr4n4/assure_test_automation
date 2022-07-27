from behave import *

from page_objects.login_page import LoginPage


@then("I verify I logged in successfully as investor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    LoginPage(context).verify_user_logged_in_as_investor()


@step("I redirect to the sign in page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    LoginPage(context).verify_login_page()


@then("I enter new account info for sign in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    LoginPage(context).enter_email_pwd(context.email)