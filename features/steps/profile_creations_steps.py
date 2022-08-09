from behave import *
from page_objects.organizerprofile_page import ProfileOrg

@then('I choose "{type}" as profile type')
def step_impl(context, type):
    """
    :type context: behave.runner.Context
    """
    ProfileOrg(context).choose_new_profile_type_as(type)


@step("I enter Authorized Tax Representative information")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ProfileOrg(context).enter_auth_tax_info()


@step("I click Create Profile for the organizer")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ProfileOrg(context).click_create_profile()


@then("I delete the new created profile for the organizer")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ProfileOrg(context).delete_profile(context.profile_type)
