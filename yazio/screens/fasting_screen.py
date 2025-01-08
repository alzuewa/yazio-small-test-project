import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class FastingScreen:
    def __init__(self):
        self.free_tracker_badge = browser.element((AppiumBy.ID, 'com.yazio.android:id/freeBadge'))
        self.free_tracker = browser.element(
            (AppiumBy.XPATH, '//*[@resource-id="com.yazio.android:id/title" and @text="16:8"]'))
        self.pro_lock = browser.element((AppiumBy.ID, 'com.yazio.android:id/proLock'))

        self.start_tracker_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/start'))
        self.cancel_tracker_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/cancel'))

        self.timer_view = browser.element((AppiumBy.ID, 'com.yazio.android:id/counter'))

        self.cycle_switch_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/action'))
        self.cycle_switch_popup = browser.element((AppiumBy.ID, 'com.yazio.android:id/md_text_message'))
        self.popup_yes_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/md_button_positive'))
        self.popup_no_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/md_button_negative'))
        self.popup_title = browser.element((AppiumBy.ID, 'com.yazio.android:id/md_text_title'))

        self.close_tracker_screen_icon = browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton'))

    @allure.step('Choosing free tracker')
    def choose_free_tracker(self):
        browser.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable('
                                                   'new UiSelector().scrollable(true).instance(0)).'
                                                   'scrollIntoView(text("free"))'
        )
        self.free_tracker.click()

    @allure.step('Starting tracker')
    def start_tracker(self):
        self.start_tracker_button.click()

    @allure.step('Switching cycle')
    def switch_cycle(self):
        self.cycle_switch_button.click()

    @allure.step('Close tracker screen')
    def close_tracker_screen(self):
        self.close_tracker_screen_icon.click()

    @staticmethod
    @allure.step('Scrolling from screen bottom to top')
    def scroll_from_bottom_to_top():
        browser.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable('
                                                   'new UiSelector().scrollable(true).instance(0)).'
                                                   'scrollIntoView(text("Intermittent Fasting"))'
        )

    @allure.step('Choosing Free tracker')
    def start_free_tracker(self):
        self.choose_free_tracker()
        self.start_tracker()

    @allure.step('Tap "Yes" on confirmation popup')
    def confirm_choice(self):
        self.popup_yes_button.click()

    @allure.step('Tap "Cancel fasting"')
    def cancel_fasting(self):
        self.cancel_tracker_button.click()
