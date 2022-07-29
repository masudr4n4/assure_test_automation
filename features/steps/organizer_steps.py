from behave import *
from static.data import *
from page_objects.deals_page import Deals
@given("I am logged in as organizer profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(f'''
    Given I am on the homepage
    And I click "Already have an account"
    And I set up cookies for the registry pop pup
    Then I enter my "{organizer_username}" and "{organizer_password}"
    And I click "SIGN IN" for login
    Then I verify I logged in successfully
    ''')


@step('I click on "New Deal"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).click_new_deals()
