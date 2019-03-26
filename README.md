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

Environmental Controls

`before_step(context, step)`, `after_step(context, step)`
These run before and after every step.

`before_scenario(context, scenario)`, `after_scenario(context, scenario)`
These run before and after each scenario is run.

`before_feature(context, feature)`, `after_feature(context, feature)`
These run before and after each feature file is exercised.

`before_tag(context, tag)`, `after_tag(context, tag)`
These run before and after a section tagged with the given name. They are invoked for each tag encountered in the order they’re found in the feature file. See controlling things with tags.

`before_all(context)`, `after_all(context)`
These run before and after the whole shooting match
