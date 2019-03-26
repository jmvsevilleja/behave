Feature: showing off behave

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  Scenario: check before all
    Given we have behave installed
    When we implement a test
    Then context server is "simple server"

  Scenario: table data scenario
    Given a set of specific users
      | name      | department  |
      | Barry     | Beer Cans   |
      | Pudey     | Silly Walks |
      | Two-Lumps | Silly Walks |

    When we count the number of people in each department
    Then we will find two people in "Silly Walks"
    But we will find one person in "Beer Cans"

  Scenario: Search for an account
    Given I search for a valid account
    Then I will see the account details

  Scenario: Invoke another step
    When I do the same thing as before

  Scenario: look up a book
    Given I search for a valid book
    Then the result page will include "success"

  Scenario: look up an invalid book
    Given I search for a invalid book
    Then the result page will include "failure"
