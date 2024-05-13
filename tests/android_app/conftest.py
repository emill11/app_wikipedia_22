from allure_commons._allure import step
import pytest
from dotenv import load_dotenv
from selene import browser
from utils import attach
from appium import webdriver
from config import config_app


def pytest_addoption(parser):
    parser.addoption("--context", action="store", default="local",
                     help="Context for load options")


def pytest_configure(config):
    context = config.getoption("--context")
    env_file = f'.env.{context}'
    load_dotenv(dotenv_path=env_file)


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    context = request.config.getoption("--context")
    options = config_app.to_driver_options(context=context)

    if context == 'bstack':
        browser.config.driver = webdriver.Remote(config_app.remote_url, options=options)
    elif context == 'local':
        browser.config.driver = webdriver.Remote(config_app.local_url,
                                                 options=options)
    browser.config.timeout = config_app.timeout

    yield

    with step('attach xml'):
        attach.attach_xml(browser)

    with step('attach screen'):
        attach.attach_screen(browser)

    if context == 'bstack':
        with step('attach video'):
            session_id = browser.driver.session_id
            attach.attach_bstack_video(session_id)

    with step('tear down app session'):
        browser.quit()
