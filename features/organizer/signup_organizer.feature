
@organizer
Feature: Sign up organizer account

  Scenario:Invite organizer and sign up
    Given I on the assure admin page
    And I invite an organizer for standard deal type
    And I am on the homepage
    And I fill out sign up information for creating new account and submit with invited email
    Then I agree with term and conditions
    And I redirect to the sign in page
    Then I enter new account info for sign in
    And I click "SIGN IN" for login
    Then I verify I logged in successfully as organizer and landed on welcome page