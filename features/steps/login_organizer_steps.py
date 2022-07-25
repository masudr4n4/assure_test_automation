from behave import *
from page_objects.login_page import LoginPage


@then('I enter my "{username}" and "{password}"')
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    LoginPage(context).enter_email_pwd(username, password)


@step('I click "{SIGN_IN}" for login')
def step_impl(context,SIGN_IN):
    """
    :type context: behave.runner.Context
    """
    LoginPage(context).click_login()


@then("I verify I logged in successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    LoginPage(context).verify_user_logged_in()

@then("I verify I am not logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    LoginPage(context).verify_user_not_logged_in()