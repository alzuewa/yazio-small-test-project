import allure
from allure_commons.types import Severity
from selene import be

from data.app_constants import OnboardingChoices as Choices, Buttons
from yazio.screens.application import app


@allure.epic('Onboarding')
@allure.story('Pass onboarding')
@allure.title('[Onboarding] Skip login')
@allure.tag('Regression')
@allure.severity(Severity.CRITICAL)
def test_pass_onboarding():
    app.onboarding_screen.wait_for_onboarding_and_start()
    app.onboarding_screen.set_main_goal(Choices.MainGoal.SOMETHING_ELSE)
    app.onboarding_screen.set_gender(Choices.Gender.FEMALE)
    app.onboarding_screen.set_secondary_goal(Choices.SecondaryGoal.BOOST_ENERGY)

    app.onboarding_screen.set_usage_purpose(Choices.UsagePurpose.ACTIVITI_TRACK)
    app.onboarding_screen.set_knowledge_level(Choices.KnowledgeLevel.ADVANCED)
    app.onboarding_screen.set_second_usage_purpose(Choices.Habits.HYDRATION)
    app.onboarding_screen.set_stoppers(Choices.Stopper.NO_TIME)

    app.onboarding_screen.set_height_units(Buttons.CM)
    app.onboarding_screen.set_activity_level(Choices.ActivityLevel.VERY_ACTIVE)
    app.onboarding_screen.set_weight(weight=65)
    app.onboarding_screen.set_diet(Choices.Diet.CLASSIC)

    app.onboarding_screen.set_destructor_bool(Choices.Choice.NO)
    app.onboarding_screen.set_trigger(Choices.Trigger.OTHER)
    app.onboarding_screen.set_strategy(Choices.Strategy.MORE_WATER)
    app.onboarding_screen.set_tactics(Choices.MealTactics.DO_NOT_KNOW, Choices.ActivityTactics.SCHEDULE_ACTIVITY)
    app.onboarding_screen.set_metrics_and_rewards(Choices.Metrics.OTHER, Choices.Celebration.OTHER)

    app.onboarding_screen.set_children(Choices.HasChildren.NO)
    app.onboarding_screen.set_schedule(Choices.Schedule.OTHER)
    app.onboarding_screen.set_habits(Choices.MatesHabits.DO_NOT_KNOW)
    app.onboarding_screen.set_support_preference(Choices.SupportPreference.NOTHING)

    app.onboarding_screen.wait_for_plan_and_continue()
    app.onboarding_screen.set_weekend_habits(Choices.Choice.NO)
    app.onboarding_screen.close_paywall()
    app.onboarding_screen.skip_login()

    with allure.step('Assert home screen opened after onboarding'):
        app.tabbar.bar.with_(timeout=10).should(be.visible)
        app.home_screen.tips_section.should(be.visible)
