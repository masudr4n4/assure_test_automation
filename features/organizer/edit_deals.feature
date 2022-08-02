# Created by HP at 02-Aug-22
Feature: Deals edition

  Scenario: Edit deal carry and management fees
    Given I am logged in as organizer profile
    And I open deal details page
    Then I move to "Carry" section and edit percentage
    And I move to "Management" section and edit percentage