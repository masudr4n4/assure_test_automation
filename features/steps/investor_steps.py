from behave import *
from static.data import investor_username, investor_password
from page_objects.investorprofile_page import InvestorProfile


@given("I am logged in as investor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(
        f"""
    Given I am on the homepage
    And I click "Already have an account"
    Then I enter my "{investor_username}" and "{investor_password}"
    And I click "SIGN IN" for login
    Then I verify I logged in successfully as investor
        """)


@step("I click New Profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).click_new_profile()


@step("I fill out information for individual profile as us citizen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.profile_type = "individual"
    InvestorProfile(context).fill_out_information_for_individual_account()


@step("I fill out information for entity LLC profile as us citizen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.profile_type = "entity"
    page = InvestorProfile(context)
    page.select_entity_profile_section()
    page.fill_out_information_for_entity_account()


@when("I submit for creating profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).submit_profile_info()


@step("I check mark Investor accreditation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).check_mark_investor_accreditation()


@step("I click Create Profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).click_create_profile()


@then("I delete the new created profile")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).delete_new_created_profile(context.profile_type)


@step("I check mark entity accreditation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).check_mark_entity_accreditation()


@step("I click Create Profile for entity")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).click_create_profile_ent()


@step("I fill out information for trust profile as us citizen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.profile_type = "trust"
    InvestorProfile(context).fill_out_information_for_trust_account()


@step("I check mark Trust accreditation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).mark_trust_accredditation()


@step("I fill out information for joint profile as us citizen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.profile_type = "joint"
    InvestorProfile(context).fill_out_information_for_joint_account()


@step("I check mark Joint accreditation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).mark_joint_accreditation()


@step("I fill out information for retirement profile as us citizen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.profile_type = "retire"
    InvestorProfile(context).fill_out_information_for_retirement_account()


@step("I check mark retirement investor accreditation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).check_retirement_investor_accreditation()


@step("I click Create Profile for retirement")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).create_profile_retirement()


@step("I fill out information for entity LP profile as us citizen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.profile_type = "entity"
    page = InvestorProfile(context)
    page.select_entity_profile_section()
    page.select_account_type_for_entity_account("LP")
    page.fill_out_information_for_entity_account()


@step("I fill out information for individual profile as non us citizen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.profile_type = "individual"
    InvestorProfile(context).fill_out_information_for_individual_account(us=False)


@step("I delete profiles if already exist for investor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    InvestorProfile(context).delete_all_profile()