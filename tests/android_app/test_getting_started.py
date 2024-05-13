from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure_commons._allure import step


def test_getting_started():
    with step('page 1'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text('The Free Encyclopedia'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('page 2'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text('New ways to explore'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('page 3'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text('Reading lists with sync'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('page 4'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text('Data & Privacy'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    with step('Start screen'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('Search Wikipedia'))
