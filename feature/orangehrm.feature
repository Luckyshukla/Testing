Feature: OrangeHRM Logo
  Scenario: logo presence on OrangeHRM home page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo present on page
    Then close browser