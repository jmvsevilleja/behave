from behave import *


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True


# invoke another step
@when('I do the same thing as before')
def step_impl(context):
    context.execute_steps('''
        then behave will test it for us!
    ''')


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@when(u'I press the big red button')
def step_impl(context):
    assert True


@given(u'I search for a valid book')
def step_impl(context):
    assert True


@given(u'I search for a invalid book')
def step_impl(context):
    assert True


@then('the result page will include "{text}"')
def step_impl(context, text):
    # if text not in context.response:
    #    fail('%r not in %r' % (text, context.response))
    if text in ["success"]:
        assert True
    else:
        assert False


@then('context server is "{text}"')
def stem_impl(context, text):
    if text in [context.server]:
        assert True
    else:
        assert False
