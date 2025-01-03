from typing import Optional

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.keyboard import Keyboard
from selene import browser


def click_element_with_text(text: str, wait: Optional[int] = None):
    if wait:
        find_element_by_text(text=text, wait=wait).click(xoffset=3, yoffset=3)
    else:
        find_element_by_text(text=text).click(xoffset=3, yoffset=3)


def find_element_by_text(text: str, wait: Optional[int] = None):
    if wait:
        return browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]')).with_(timeout=wait)
    else:
        return browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="{text}"]'))


def hide_keyboard():
    Keyboard().hide_keyboard()
