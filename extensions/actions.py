
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

import TestCases.conftest
from TestCases.conftest import action


class actions:
    def click_action(element: WebElement):
        element.click()

    def sendkeys_action(element: WebElement, value: str):
        element.send_keys(value)

    def mouseover_action(element1: WebElement, element2: WebElement):
        TestCases.conftest.action(element1).move_to_element(element2).click().perform()

    def drag_and_drop_action(start: WebElement, end: WebElement):
        action.drag_and_drop(start, end).perform()

    def clear_action(element: WebElement):
        element.clear()


    def element_value(element: WebElement):
        return element.get_property('value')


    def element_text(element: WebElement):
        return element.text

    def select_by_value(select_element:WebElement,value):
        Select(select_element).select_by_value(value)


    def select_by_index(select_element: WebElement, index):
        Select(select_element).select_by_index(index)


    def select_by_text(select_element: WebElement, text):
        Select(select_element).select_by_visible_text(text)

