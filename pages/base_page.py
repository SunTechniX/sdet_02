from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def click_to_element(self, locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()

    def get_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        # return self.browser.find_element(*locator)

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def scroll_to_element(self, element):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)

    def write_to_element(self, locator, text, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator)).send_keys(text)
        # self.get_element(locator).send_keys(text)
