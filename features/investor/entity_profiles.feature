# Created by HP at 03-Aug-22
@investor
Feature: Investor profiles entity

  @create_profile @creat_entity_profile @LLC
  Scenario: Create an LLC entity profile for investor and delete
    Given I am logged in as investor
    And I moved to profile section
    And I delete profiles if already exist for investor
    And I click New Profile
    And I fill out information for entity LLC profile as us citizen
    And I check mark entity accreditation
    And I click Create Profile for entity
    Then I delete the new created profile

  @create_profile @creat_entity_profile @LP
  Scenario: Create an LP entity profile for investor and delete
    Given I am logged in as investor
    And I moved to profile section
    And I click New Profile
    And I fill out information for entity LP profile as us citizen
    And I check mark entity accreditation
    And I click Create Profile for entity
    Then I delete the new created profile