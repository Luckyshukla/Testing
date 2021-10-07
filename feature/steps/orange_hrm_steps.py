from behave import *
from selenium import webdriver
@given(u'launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when(u'open orange hrm homepage')
def hrm_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divlogo']//img").is_displayed()
    assert status is True


@then(u'close browser')
def close_browser(context):
    context.driver.close()