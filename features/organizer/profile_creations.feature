
@organizer
Feature: Profile creation for organizer
  # Enter feature description here
  @create_profile @individual_profile
  Scenario: Create new Organizer individual profile
    Given I am logged in as organizer profile for creating profile
    And I moved to profile section
    And I click for New Organizer Profile
    Then I choose "Individual" as profile type
    And I fill out information for individual profile as us citizen
    And I enter Authorized Tax Representative information
    And I click Create Profile for the organizer
    Then I delete the new created profile for the organizer