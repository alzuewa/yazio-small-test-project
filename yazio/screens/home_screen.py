import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class HomeScreen:
    def __init__(self):
        self.tips_section = browser.element((AppiumBy.CLASS_NAME, 'android.widget.HorizontalScrollView'))
        self.tips = browser.all((AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.View'))

        self.streak_icon = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Opens your streak overview'))
        self.streak_counter = browser.element(
            (AppiumBy.XPATH, '//*[@content-desc="Opens your streak overview"]/../android.widget.TextView'))

        self.breakfast = browser.element((AppiumBy.XPATH, '//*[@text="Breakfast"]'))
        self.lunch = browser.element((AppiumBy.XPATH, '//*[@text="Lunch"]'))
        self.dinner = browser.element((AppiumBy.XPATH, '//*@text="Dinner"]'))
        self.snaks = browser.element((AppiumBy.XPATH, '//*[@text="Snacks"]'))
        self.add_more_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/addMore'))

        self.fasting_now_label = browser.element((AppiumBy.XPATH, '//*[@text="🦊 Now: Fasting"]'))
        self.eating_now_label = browser.element((AppiumBy.XPATH, '//*[@text="🦊 Now: Eating"]'))

        self.eaten_counter = browser.element((AppiumBy.XPATH, '//*[@text="Eaten"]/../android.widget.TextView[1]'))

    @allure.step('Click on lunch to add meals')
    def open_luch_to_add(self):
        self.lunch.click()
        self.add_more_button.click()

    @allure.step('Get "Eaten" value')
    def get_eaten_value(self):
        value = self.eaten_counter.locate().text
        return int(value)

    @allure.step('Get streak value')
    def get_streak_value(self):
        value = self.streak_counter.locate().text
        return int(value)
