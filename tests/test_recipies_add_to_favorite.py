import allure
from allure_commons.types import Severity
from selene import be

from yazio.screens.application import app


@allure.epic('Favorite recipes')
@allure.story('Add recipe to favorite')
@allure.title('[Favorites] Add recipe')
@allure.tag('Regression')
@allure.severity(Severity.MINOR)
def test_add_favorites_from_categories(open_home):
    with allure.step('Open recipes screen and check "Favorites" list'):
        app.tabbar.open_recipies_screen()
        app.recipies_screen.switch_to_favorites()

    with allure.step('Assert "Favorites" list is empty'):
        app.recipies_screen.favorites_empty_tab.should(be.visible)

    with allure.step('Add dish of the day to "Favorites"'):
        app.recipies_screen.switch_to_discover()
        app.recipies_screen.open_breakfast_category()
        app.recipies_screen.mark_dish_of_the_day_favorite()

    with allure.step('Assert "Favorites" list is not empty'):
        app.recipies_screen.dish_starred.should(be.visible)
        app.recipies_screen.click_back()
        app.recipies_screen.switch_to_favorites()
        app.recipies_screen.favorites_empty_tab.should(be.not_.visible)

    with allure.step('Remove dish from "Favorites"'):
        app.recipies_screen.unmark_favorite_dish()

    with allure.step('Assert "Favorites" list is empty'):
        app.recipies_screen.favorites_empty_tab.should(be.visible)
