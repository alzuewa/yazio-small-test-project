import allure
from allure_commons.types import Severity
from selene import be

from yazio.screens.application import app


@allure.epic('Diary')
@allure.story('Add records to diary')
@allure.title('[Diary] Add meals from presets')
@allure.tag('Regression')
@allure.severity(Severity.CRITICAL)
def test_tracker_meals(open_home):
    app.home_screen.open_luch_to_add()

    with allure.step('Assert country confirmation is shown'):
        app.meal_screen.country_confirmation_banner.should(be.visible)
        app.meal_screen.confirm_button.click()

    with allure.step('Add product'):
        app.meal_screen.add_product_on_position(position=2)

    with allure.step('Assert "Eaten" counter has increased'):
        assert app.home_screen.get_eaten_value() != 0

    with allure.step('Assert "Streak" counter has increased'):
        assert app.home_screen.get_streak_value() == 1
