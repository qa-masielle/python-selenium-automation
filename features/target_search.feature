Feature: Target product search

    Scenario Outline: Search for product on Target
        Given Open Target homepage
        When Search Target for "<item>"
        Then Target search results contain "<item>"

      Examples:
          | item |
          | mug |
          | lego |