Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open Orange HRM homepage
    And Enter user name "admin" and password "admin123"
    And click on login button
    Then User must successfully login to dashboard page


  Scenario Outline:  Login to OrangeHRM with Multiple parameters
    Given I launch Chrome browser
    When I open Orange HRM homepage
    And Enter user name "<username>" and password "<password>"
    And click on login button
    Then User must successfully login to dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | user     | adm23    |
      | admin    | make123f |
      | xenon    | xenon123 |

