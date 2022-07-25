# Created by HP at 23-Jul-22
Feature: Login organizer profile

  Scenario Outline: Testing different scenario for organizer positive login scenario
    Given I am on the homepage
    And I click "Already have an account"
    Then I enter my "<username>" and "<password>"
    And I click "SIGN IN" for login
    Then I verify I logged in successfully
    Examples:
    |         username          | password     |
#    |123@mailinator.com         | Testing@12345|
    |org.acc04apr@yopmail.com   | Apple@1234567|
    |testacc1@yopmail.com       | Testaccount1!|
    | rana@alagzoo.com          | Testaccount1!@|

  Scenario Outline: Testing different scenario for organizer negative login scenario
    Given I am on the homepage
    And I click "Already have an account"
    Then I enter my "<username>" and "<password>"
    And I click "SIGN IN" for login
    Then I verify I am not logged in
    Examples:
    |         username           | password        |
    |org.accfdsf04apr@yopmail.com|Apple@1sdfd234567|
    |org.acc04apr@yopmail.com    |  empty          |
    |       empty                |  empty          |
    |       empty                |Apple@1234567    |



