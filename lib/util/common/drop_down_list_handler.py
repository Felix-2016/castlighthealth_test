from selenium.webdriver.support.select import Select


def select_ddl_by_index(element_ddl, index):
    sct = Select(element_ddl)
    sct.select_by_index(index)


def select_ddl_by_visible_text(element_ddl, text):
    sct = Select(element_ddl)
    sct.select_by_visible_text(text)


def select_ddl_by_value(element_ddl, value):
    sct = Select(element_ddl)
    sct.select_by_value(value)
