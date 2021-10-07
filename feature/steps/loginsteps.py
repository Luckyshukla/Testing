from behave import *
from selenium import webdriver


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'I open Orange HRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter user name "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must successfully login to dashboard page')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    assert text == "Dashboard"
    context.driver.close()
