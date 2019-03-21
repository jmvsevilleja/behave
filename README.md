# behave

Website: https://behave.readthedocs.io


Create Virtual Environment:
    `python3 -m venv ~/.virtualenvs/behave`
    win: `mkvirtualenv behave`

Activate Environment:
    `source ~/.virtualenvs/behave/bin/activate`
    win: `workon behave`

Install Behave
    `pip install behave`

```feature
Scenario

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
        context.text
        """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
        context.table
        | name      | department  |
        | Barry     | Beer Cans   |
        | Pudey     | Silly Walks |
        | Two-Lumps | Silly Walks |
    When attacked by Chuck Norris
    Then the ninja should run for his life
    And fall off a cliff

Scenario Outline

Scenario Outline: Blenders
   Given I put <thing> in a blender,
    when I switch the blender on
    then it should transform into <other thing>

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | mush        |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |

Step Parameters

Scenario: look up a book
  Given I search for a valid book
   Then the result page will include "success"

Scenario: look up an invalid book
  Given I search for a invalid book
   Then the result page will include "failure"

```
Parsers
parse (the default, based on: parse) - `{param:Type}`
cfparse (extends: parse, requires: parse_type) -
re - regular expressions
use_step_matcher()

Context - variable that’s passed around

context.table
context.text
context.failed - any step fails

