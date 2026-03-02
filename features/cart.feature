Feature: Target Cart Functionality

  Scenario: Verify empty cart message
    Given I open target.com
    When I click on the cart icon
    Then I should see "Your cart is empty"