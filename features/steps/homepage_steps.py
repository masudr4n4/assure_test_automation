from behave import *
from page_objects.home_page import HomePage
from time import sleep

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

@step("I set up cookies for the registry pop pup")
def step_add_value(context):
    context.browser.execute_script("""window.localStorage['li_ignored'] = '[{"id":3312863,"time":1659063687591}]'""")

@step('I wait some seconds')
def step_impl(context):
    """
    :param button_text:
    :type context: behave.runner.Context
    """
    sleep(20)
