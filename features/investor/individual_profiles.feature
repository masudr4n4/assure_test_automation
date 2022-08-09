@investor
Feature: Investor profiles individuals
  @create_profile @create_individual_profile
  Scenario: Create an individual profile for investor and delete as us citizen
    Given I am logged in as investor
    And I moved to profile section
    And I click New Profile
    And I fill out information for individual profile as us citizen
    When I submit for creating profile
    And I check mark Investor accreditation
    And I click Create Profile
    Then I delete the new created profile

  Scenario: Create an individual profile for investor as non-Us and delete
    Given I am logged in as investor
    And I moved to profile section
    And I click New Profile
    And I fill out information for individual profile as non us citizen
    When I submit for creating profile
    And I check mark Investor accreditation
    And I click Create Profile
    Then I delete the new created profile


