import os
from datetime import datetime

import allure
import allure_commons
import pytest
import selene
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser

from config import project_config
from utils import attach
from yazio.screens.application import app


def pytest_addoption(parser):
    parser.addoption('--context', action='store', required=True)


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    context = request.config.getoption('--context')

    options = UiAutomator2Options().load_capabilities(project_config.get_env(context))
    if context == 'bstack':
        options.set_capability(
            name='bstack:options',
            value={
                'projectName': 'Automation project',
                'buildName': f'browserstack-build-{datetime.now()}',
                'sessionName': request.node.name,
                'userName': os.getenv('BSTACK_USER_NAME'),
                'accessKey': os.getenv('BSTACK_ACCESS_KEY')
            }
        )

    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'),
                                                 options=options
                                                 )

    browser.config.timeout = float(project_config.DRIVER_TIMEOUT)
    browser.config._wait_decorator = selene.support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield driver

    attach.add_screenshot()
    attach.add_page_source()
    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    if context == 'bstack':
        attach.add_bstack_video(session_id)


@pytest.fixture(scope='function')
def open_home(driver):
    app.tabbar.open_home_screen()

    yield
