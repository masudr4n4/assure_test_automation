@investor
Feature: Login investor profile
  @login
  Scenario Outline: Testing different scenario for investor positive login scenario
    Given I am on the homepage
    And I click "Already have an account"
    Then I enter my "<username>" and "<password>"
    And I click "SIGN IN" for login
    Then I verify I logged in successfully as investor
    Examples:
    |         username          | password     |
    |testixx@assure.com         | TestAccountPwd2@|
    |testwik@assure.com         | newPassswrod4v@|
