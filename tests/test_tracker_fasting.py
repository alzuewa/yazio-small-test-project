import allure
from allure_commons.types import Severity
from selene import be, have

from yazio.screens.application import app


@allure.epic('Fasting')
@allure.story('Start, stop, cancel fasting')
@allure.title('[Fasting] 16/8')
@allure.tag('Regression')
@allure.severity(Severity.NORMAL)
def test_tracker_fasting(open_home):
    with allure.step('Choose and start free fasting tracker'):
        app.tabbar.open_fasting_screen()
        app.fasting_screen.start_free_tracker()

    with allure.step('Assert tracker is actually started'):
        app.fasting_screen.timer_view.should(be.visible)
        app.fasting_screen.cycle_switch_button.should(have.text('START FASTING'))

    with allure.step('Assert started eating is shown in home screen'):
        app.tabbar.open_home_screen()
        app.home_screen.eating_now_label.should(be.visible)

    with allure.step('Switch tracker from eating to fasting'):
        app.tabbar.open_fasting_screen()
        app.fasting_screen.switch_cycle()

    with allure.step('Assert confirmation popup is shown'):
        app.fasting_screen.cycle_switch_popup.should(be.visible)

    with allure.step('Agree to stop fasting slot'):
        app.fasting_screen.confirm_choice()

    with allure.step('Assert button text has correctly changed'):
        app.fasting_screen.cycle_switch_button.should(have.text('END FASTING'))

    with allure.step('Assert fasting time is shown on the home screen'):
        app.tabbar.open_home_screen()
        app.home_screen.fasting_now_label.should(be.visible)

    with allure.step('Cancelling fasting tracker completely'):
        app.tabbar.open_fasting_screen()
        app.fasting_screen.choose_free_tracker()
        app.fasting_screen.cancel_tracker_button.should(be.visible)
        app.fasting_screen.cancel_fasting()

    with allure.step('Assert confirmation popup is shown'):
        app.fasting_screen.popup_title.should(have.text('Cancel Fast'))

    with allure.step('Agree to cancel fasting'):
        app.fasting_screen.confirm_choice()

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
