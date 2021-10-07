Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open Orange HRM homepage
    And Enter user name "admin" and password "admin123"
    And click on login button
    Then User must successfully login to dashboard page