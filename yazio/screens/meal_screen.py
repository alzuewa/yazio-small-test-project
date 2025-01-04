import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class AddMealScreen():
    def __init__(self):
        self.add_more_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/addMore'))

        self.country_confirmation_banner = browser.element(
            (AppiumBy.XPATH, '//*[@text="Are you currently shopping in this country?"]'))
        self.confirm_button = browser.element((AppiumBy.XPATH, '//*[@text="CONFIRM"]'))

        self.add_product_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/addButton'))
        self.done_button = browser.element((AppiumBy.ID, 'com.yazio.android:id/loggingDone'))
        self.back_button = browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton'))

    @allure.step('Confirm country')
    def confirm_country(self):
        self.confirm_button.click()

    @allure.step('Add product on {position} position in list')
    def add_product_on_position(self, position):
        product = browser.element(
            (
                AppiumBy.XPATH,
                f'//*[@resource-id="com.yazio.android:id/recycler"]/android.view.ViewGroup[{position}]'
            )
        )
        product.click()
        self.add_product_button.click()
        self.done_button.click()
        self.back_button.click()
