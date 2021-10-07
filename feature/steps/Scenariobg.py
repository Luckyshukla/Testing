from behave import *


@given('I launched browser')
def step_impl(context):
    assert True, "Test Passed"


@when('I open application')
def step_impl(context):
    assert True, "Test passed"

@when('Enter valid username and Password')
def step_impl(context):
    assert True, "Test Passed"


@when('click on login')
def step_impl(context):
    assert True, "Test Passed"


@then('User must login to the Dashboard page')
def step_impl(context):
    assert True, "Test Passed"


@when(u'navigate to search path')
def step_impl(context):
    assert True, "Test Passed"


@then('Search page should be displayed')
def step_impl(context):
    assert True, "Test Passed"


@when(u'navigate to advance search page')
def step_impl(context):
    assert True, "Test Passed"


@then('Advance search page should be Displayed')
def step_impl(context):
    assert True, "Test Passed"
