import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser


class RecipesScreen:

    def __init__(self):
        self.day_dish_empty_star = browser.element(
            (AppiumBy.XPATH, '(//android.view.View[@content-desc="Mark as favorite"])[1]'))
        self.dish_starred = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Unmark as favorite'))
        self.breakfast_category = browser.element((AppiumBy.XPATH, '//*[@text="Breakfast"]'))

        self.favorites_tab = browser.element((AppiumBy.XPATH, '//*[@text="FAVORITES"]'))
        self.discover_tab = browser.element((AppiumBy.XPATH, '//*[@text="DISCOVER"]'))
        self.favorites_empty_tab = browser.element((AppiumBy.XPATH, '//*[@text="No favorite recipes yet?"]'))

        self.back_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Back'))

    @allure.step('Mark dish of the day as favorite')
    def mark_dish_of_the_day_favorite(self):
        self.day_dish_empty_star.click()

    @allure.step('Unmark the only favorite dish')
    def unmark_favorite_dish(self):
        self.dish_starred.click()

    @allure.step('Mark dish as favorite by number in list. Number {count}')
    def mark_recipe_favorite(self, count):
        browser.element((AppiumBy.XPATH, f'(//android.view.View[@content-desc="Mark as favorite"])[{count}]'))

    @allure.step('Switch to FAVORITES tab')
    def switch_to_favorites(self):
        self.favorites_tab.click()

    @allure.step('Switch to DISCOVER tab')
    def switch_to_discover(self):
        self.discover_tab.click()

    @allure.step('Open Breakfast category')
    def open_breakfast_category(self):
        self.breakfast_category.click()

    @allure.step('Check dish {query} in search results')
    def dish_in_search_results(self, query):
        dish = browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="{query}"]'))
        return dish.should(be.visible)

    @allure.step('Check dish {query} in favorites list')
    def dish_in_favorites_list(self, query):
        dish = browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="{query}"]'))
        return dish.should(be.visible)

    @allure.step('Click back button')
    def click_back(self):
        self.back_button.click()
