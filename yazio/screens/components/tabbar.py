import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class Tabbar:

    def __init__(self):
        self.bar = browser.element((AppiumBy.ID, 'com.yazio.android:id/bottomNav'))
        self.diary_tab = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Diary'))
        self.fasting_tab = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Fasting'))
        self.recipes_tab = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Recipes'))
        self.profile_tab_with_notification = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Profile, New notification'))
        self.profile_tab = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Profile'))
        self.pro_tab = browser.element((AppiumBy.ACCESSIBILITY_ID, 'PRO'))

    @allure.step('Open Diary screen')
    def open_home_screen(self):
        self.diary_tab.click()

    @allure.step('Open Fasting tracker screen')
    def open_fasting_screen(self):
        self.fasting_tab.click()

    @allure.step('Open Recipes screen')
    def open_recipies_screen(self):
        self.recipes_tab.click()
