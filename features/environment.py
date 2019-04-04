# -- FILE: features/environment.py
from behave import fixture, use_fixture
from fixtures import wsgi_server
from selenium import webdriver
import platform


@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    if(platform.system() == 'Windows'):
        context.browser = webdriver.Chrome('chromedriver.exe')
    elif(platform.system() == 'Linux'):
        context.browser = webdriver.Chrome('chromedriver')

    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    use_fixture(wsgi_server, context, port=8000)
    use_fixture(selenium_browser_chrome, context)
    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.


def before_feature(context, feature):
    context.server = 'complicated server'
    # model.init(environment='test')
