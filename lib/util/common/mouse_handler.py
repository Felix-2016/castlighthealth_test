from selenium.webdriver import ActionChains


def mouse_hover_on_element(browser, element):
    act = ActionChains(browser)
    act.move_to_element(element).perform()


def double_click_on_element(browser, element):
    act = ActionChains(browser)
    act.double_click(element).perform()


def context_click_on_element(browser, element):
    act = ActionChains(browser)
    act.context_click(element).perform()


def drag_and_drop(browser, source_element, target_element):
    act = ActionChains(browser)
    act.drag_and_drop(source_element, target_element).perform()
