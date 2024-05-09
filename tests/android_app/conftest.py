import pytest
from selene import browser
from utils import attach
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils import file


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    remote_url = 'http://127.0.0.1:4723'
    app_wait_activity = 'org.wikipedia.*'
    app = './app-alpha-universal-release.apk'

    options = UiAutomator2Options()
    options.set_capability('remote_url', remote_url)
    options.set_capability('appWaitActivity', app_wait_activity)
    options.set_capability('app', file.path_apk(app))

    browser.config.driver = webdriver.Remote(remote_url, options=options)
    browser.config.timeout = 10.0

    yield

    attach.attach_screen(browser)
    attach.attach_xml(browser)

    browser.quit()
