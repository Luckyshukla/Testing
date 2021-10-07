Feature: OrangeHRM Login
  Background: common steps
    Given I launched browser
    When I open application
    And Enter valid username and Password
    And click on login
  Scenario: Login to HRM Application
    Then User must login to the Dashboard page
  Scenario: Search User
    When navigate to search path
    Then Search page should be displayed
  Scenario: Advanced Search user
    When navigate to advance search page
    Then Advance search page should be Displayed