@investor
Feature: Investor profiles retirement

  @create_profile
  Scenario: Create an retirement profile for investor and delete
    Scenario: Create an individual profile for investor and delete
    Given I am logged in as investor
    And I moved to profile section
    And I click New Profile
    And I fill out information for retirement profile as us citizen
    And I check mark retirement investor accreditation
    And I click Create Profile for retirement
    Then I delete the new created profile