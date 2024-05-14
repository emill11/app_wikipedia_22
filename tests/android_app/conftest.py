from allure_commons._allure import step
import pytest
from dotenv import load_dotenv
from selene import browser
from utils import attach, path
from appium import webdriver
from config import Config


def pytest_addoption(parser):
    parser.addoption("--context", action="store", default="bstack",
                     help="Context for load options")


def pytest_configure(config):
    context = config.getoption("--context")
    env_file = path.root_path(f'.env.{context}')
    load_dotenv(env_file)


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    app_context = request.config.getoption("--context")
    config_app = Config()
    app_options = config_app.to_driver_options(context=app_context)
    browser.config.driver = webdriver.Remote(config_app.url, options=app_options)
    browser.config.timeout = config_app.timeout

    yield

    with step('attach xml'):
        attach.attach_xml(browser)

    with step('attach screen'):
        attach.attach_screen(browser)

    if app_context == 'bstack':
        with step('attach video'):
            session_id = browser.driver.session_id
            attach.attach_bstack_video(session_id)

    with step('`tear down app session'):
        browser.quit()
