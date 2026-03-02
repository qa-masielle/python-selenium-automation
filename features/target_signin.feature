Feature: Target Sign In navigation

  Scenario: Logged out user can open Sign In form
    Given I open target.com
    When I click Sign In
    And from the side menu I click Sign In
    Then I should see the Sign In form