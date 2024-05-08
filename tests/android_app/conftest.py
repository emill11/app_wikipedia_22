import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from dotenv import load_dotenv
import os
import utils.allure
from appium import webdriver
import allure

# url = "http://127.0.0.1:4723/wd/hub"
url = "http://127.0.0.1:4723/"


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({

        "appium:appWaitActivity": "org.wikipedia.*",
        "appium:app": "\\Users\\abdrakhmanovea\\Downloads\\app-alpha-universal-release.apk"

    })

    browser.config.driver_remote_url = url

    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config.driver = webdriver.Remote(url, options=options)

    yield

    browser.quit()
