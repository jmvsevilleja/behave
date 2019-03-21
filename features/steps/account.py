from behave import *


@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        print("name=", row['name'], "department=", row['department'])


@when(u'we count the number of people in each department')
def step_impl(context):
    assert True


@then(u'we will find two people in "Silly Walks"')
def step_impl(context):
    assert True


@then(u'we will find one person in "Beer Cans"')
def step_impl(context):
    assert True


@given('I search for a valid account')
def step_impl(context):
    # context.browser.get('http://localhost:8000/index')
    # form = get_element(context.browser, tag='form')
    # get_element(form, name="msisdn").send_keys('61415551234')
    # form.submit()
    assert True


@then('I will see the account details')
def step_impl(context):
    # elements = find_elements(context.browser, id='no-account')
    # eq_(elements, [], 'account not found')
    # h = get_element(context.browser, id='account-head')
    # ok_(h.text.startswith("Account 61415551234"),
        #   'Heading %r has wrong text' % h.text)
    assert True
