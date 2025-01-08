import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser

from data.app_strings import Buttons
from yazio.common_actions import find_element_by_text, click_element_with_text


class OnboardingScreen:

    def __init__(self):
        self.progress_bar = browser.element((AppiumBy.CLASS_NAME, 'android.widget.ProgressBar'))
        self.input_field = browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText'))
        self.birthday_field = browser.all(
            (AppiumBy.XPATH, '//android.widget.ScrollView//android.widget.TextView')).second
        self.back_arrow = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Back'))

    @staticmethod
    @allure.step('Choose an answer: {choice}')
    def make_choice(choice: str):
        click_element_with_text(text=choice)
        time.sleep(0.2)

    @staticmethod
    @allure.step('Click on button with text: {button_text} to continue')
    def continue_onboarding(button_text: str, wait: int = None):
        if wait:
            click_element_with_text(text=button_text, wait=wait)
            time.sleep(0.5)
        else:
            click_element_with_text(text=button_text)
            time.sleep(0.5)

    @staticmethod
    @allure.step(f'Wait for [{Buttons.GET_STARTED}] button and start onboarding')
    def wait_for_onboarding_and_start():
        start_button = find_element_by_text(text=Buttons.GET_STARTED, wait=20)
        start_button.should(be.visible)
        start_button.click()

    @staticmethod
    @allure.step('Setting main goal: {goal}')
    def set_main_goal(goal: str):
        OnboardingScreen.make_choice(goal)

    @staticmethod
    @allure.step('Setting secondary goal: {goal}')
    def set_secondary_goal(goal: str):
        OnboardingScreen.make_choice(goal)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)

    @staticmethod
    @allure.step('Setting gender: {gender}')
    def set_gender(gender: str):
        OnboardingScreen.make_choice(gender)
        OnboardingScreen.continue_onboarding(button_text=Buttons.LETS_GO)
        OnboardingScreen.continue_onboarding(button_text=Buttons.GOT_IT)

    @staticmethod
    @allure.step('Setting app usage purpose: {purpose}')
    def set_usage_purpose(purpose: str):
        OnboardingScreen.make_choice(purpose)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)

    @staticmethod
    @allure.step('Setting app knowledge level: {level}')
    def set_knowledge_level(level: str):
        OnboardingScreen.make_choice(level)

    @allure.step('Setting another app usage purpose: {purpose}')
    def set_second_usage_purpose(self, purpose: str):
        OnboardingScreen.make_choice(purpose)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)

    @staticmethod
    @allure.step('Setting current stoppers: {stopper}')
    def set_stoppers(stopper: str):
        OnboardingScreen.make_choice(stopper)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)
        OnboardingScreen.continue_onboarding(button_text=Buttons.GOT_IT)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)

    @staticmethod
    @allure.step('Setting height units: {units}')
    def set_height_units(units: str):
        OnboardingScreen.continue_onboarding(units)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)

    @staticmethod
    @allure.step('Setting activity level: {level}')
    def set_activity_level(level: str):
        OnboardingScreen.make_choice(level)

    @staticmethod
    @allure.step('Setting diet: {diet}')
    def set_diet(diet: str):
        OnboardingScreen.make_choice(diet)
        OnboardingScreen.continue_onboarding(button_text=Buttons.CANNOT_WAIT)

    @staticmethod
    @allure.step('Setting destructor presence: {answer}')
    def set_destructor_bool(answer: str):
        OnboardingScreen.make_choice(answer)

    @staticmethod
    @allure.step('Setting trigger: {trigger}')
    def set_trigger(trigger: str):
        OnboardingScreen.make_choice(trigger)
        OnboardingScreen.continue_onboarding(button_text=Buttons.GREAT)

    @staticmethod
    @allure.step('Setting tactics: for meal - {meal}, for activities - {activities}')
    def set_tactics(meal: str, activities):
        OnboardingScreen.make_choice(meal)
        OnboardingScreen.make_choice(activities)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)
        OnboardingScreen.continue_onboarding(button_text=Buttons.CONTINUE)

    @staticmethod
    @allure.step('Setting strategy: {strategy}')
    def set_strategy(strategy: str):
        OnboardingScreen.make_choice(strategy)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)

    @staticmethod
    @allure.step('Setting metrics: {metrics} and rewards - {rewards}')
    def set_metrics_and_rewards(metrics: str, rewards):
        OnboardingScreen.make_choice(metrics)
        OnboardingScreen.make_choice(rewards)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT)
        OnboardingScreen.continue_onboarding(button_text=Buttons.CONTINUE)

    @staticmethod
    @allure.step('Setting children: {response}')
    def set_children(response: str):
        OnboardingScreen.make_choice(response)

    @staticmethod
    @allure.step('Setting work schedule: {schedule}')
    def set_schedule(schedule: str):
        OnboardingScreen.make_choice(schedule)
        OnboardingScreen.continue_onboarding(button_text=Buttons.GREAT)

    @staticmethod
    @allure.step('Share mates habits: {habits}')
    def set_habits(habits: str):
        OnboardingScreen.make_choice(habits)
        OnboardingScreen.continue_onboarding(button_text=Buttons.CONTINUE)

    @staticmethod
    @allure.step('Setting support preferences: {preferences}')
    def set_support_preference(preferences: str):
        OnboardingScreen.make_choice(preferences)
        OnboardingScreen.continue_onboarding(button_text=Buttons.CREATE_PLAN)

    @staticmethod
    @allure.step('Setting weekend habits: {habits}')
    def set_weekend_habits(habits: str):
        OnboardingScreen.make_choice(habits)
        OnboardingScreen.continue_onboarding(button_text=Buttons.CONTINUE)
        OnboardingScreen.continue_onboarding(button_text=Buttons.CONTINUE)
        time.sleep(0.5)

    @allure.step('Set current weight: {weight}')
    def set_weight(self, weight: int):
        click_element_with_text(Buttons.KG)
        self.input_field.clear().type(str(weight))
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT, wait=5)
        time.sleep(0.5)
        OnboardingScreen.continue_onboarding(button_text=Buttons.NEXT, wait=5)

    @staticmethod
    @allure.step(f'Wait for personal plan to be generated and continue')
    def wait_for_plan_and_continue():
        click_element_with_text(text=Buttons.LOVE_IT, wait=20)
        time.sleep(1)
        OnboardingScreen.continue_onboarding(button_text=Buttons.LETS_GO)

    @staticmethod
    @allure.step('Skip login')
    def skip_login():
        click_element_with_text(text=Buttons.SKIP)

    @allure.step('Close paywall')
    def close_paywall(self):
        self.back_arrow.with_(timeout=6).click(xoffset=1, yoffset=1)
