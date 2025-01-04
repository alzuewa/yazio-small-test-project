import allure
from selene import be, have

from yazio.screens.application import app


def test_tracker_fasting(open_home):
    with allure.step('Choose and start free fasting tracker'):
        app.tabbar.open_fasting_screen()
        app.fasting_screen.start_free_tracker()

    with allure.step('Assert tracker is actually started'):
        app.fasting_screen.timer_view.should(be.visible)
        app.fasting_screen.cycle_switch_button.should(have.text('END FASTING'))

    with allure.step('Assert started fasting is shown in home screen'):
        app.tabbar.open_home_screen()
        app.home_screen.fasting_now_label.should(be.visible)

    with allure.step('Switch tracker from fasting to eating'):
        app.tabbar.open_fasting_screen()
        app.fasting_screen.cycle_switch_button.click()

    with allure.step('Assert confirmation popup is shown'):
        app.fasting_screen.cycle_switch_popup.should(be.visible)
        app.fasting_screen.popup_yes_button.click()

    with allure.step('Assert button text has correctly changed'):
        app.fasting_screen.cycle_switch_button.should(have.text('START FASTING'))

    with allure.step('Assert eating time is shown on the home screen'):
        app.tabbar.open_home_screen()
        app.home_screen.eating_now_label.should(be.visible)

    with allure.step('Cancel tracker'):
        app.tabbar.open_fasting_screen()
        app.fasting_screen.choose_free_tracker()
        app.fasting_screen.cancel_tracker_button.should(be.visible)
        app.fasting_screen.cancel_tracker_button.click()

    with allure.step('Assert confirmation popup is shown'):
        app.fasting_screen.popup_title.should(have.text('Cancel Fast'))
        app.fasting_screen.popup_yes_button.click()

    with allure.step('Assert action button changed its state'):
        app.fasting_screen.start_tracker_button.should(be.visible)

    with allure.step('Assert tracker timer is absent'):
        app.fasting_screen.close_tracker_screen()
        app.fasting_screen.scroll_from_bottom_to_top()
        app.fasting_screen.timer_view.should(be.not_.visible)

    with allure.step('Assert no fasting labels are shown on the home screen'):
        app.tabbar.open_home_screen()
        app.home_screen.fasting_now_label.should(be.not_.visible)
        app.home_screen.eating_now_label.should(be.not_.visible)