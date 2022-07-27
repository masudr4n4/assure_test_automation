# Created by HP at 26-Jul-22
Feature:Testing the sign up functionality
  # Enter feature description here

  Scenario: Sign up as investor account
    Given I on a deal invitation page on sign up purpose
    And I fill out sign up information for creating new account and submit
    Then I agree with term and conditions
    And I redirect to the sign in page
    Then I enter new account info for sign in
    And I click "SIGN IN" for login
    Then I verify I logged in successfully as investor