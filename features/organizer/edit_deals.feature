# Created by HP at 02-Aug-22
@organizer
Feature: Deals edition
  @edit_deal
  Scenario: Edit deal carry and management fees
    Given I am logged in as organizer profile
    And I open a deal details page
    Then I move to "Carry" section and edit percentage
    And I move to "Management" section and edit percentage

  @invite_investor
  Scenario: Send invitation for to investor to their email
    Given I am logged in as organizer profile
    And I open a deal details page
    And I click on "Invite" to invite investor for the deal
    Then I insert email addresses and Click Send invite
    And I verify invitation sent success message