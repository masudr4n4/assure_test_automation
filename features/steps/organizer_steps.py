from behave import *
from static.data import *
from page_objects.deals_page import Deals
from page_objects.home_page import HomePage
from page_objects.organizerprofile_page import ProfileOrg
from page_objects.admin_page import Admin

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


@step("I moved to profile section")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    HomePage(context).go_to_profiles()


@step("I click for New Organizer Profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ProfileOrg(context).click_create_new_org_profile()


@step("I open a deal details page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).open_first_deal()


@then('I move to "Carry" section and edit percentage')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).edit_carry_percentage()


@step('I move to "Management" section and edit percentage')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Deals(context).edit_management_percentage()


@given("I am logged in as organizer profile for creating profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(f'''
    Given I am on the homepage
    And I click "Already have an account"
    And I set up cookies for the registry pop pup
    Then I enter my "{profile_creator_org_username}" and "{password}"
    And I click "SIGN IN" for login
    Then I verify I logged in successfully
    ''')


@given("I on the assure admin page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Admin(context).logged_in_admin()


@step("I invite an organizer for standard deal type")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.email = Admin(context).send_invitation_for_org()