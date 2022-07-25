from behave import *
from page_objects.home_page import HomePage

@given("I am on the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    HomePage(context).go_to_homepage()

@step('I click "{button_text}"')
def step_impl(context, button_text):
    """
    :param button_text:
    :type context: behave.runner.Context
    """
    HomePage(context).click_login()