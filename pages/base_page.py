from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_url(self):
        self.browser.get(self.url)

    def is_element_present(self, locator, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def click_to_element(self, locator):
        self.get_element(locator).click()

    def get_element(self, locator):
        return self.browser.find_element(*locator)

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def run_script(self, script, element):
        self.browser.execute_script(script, element)

    def write_to_element(self, locator, text):
        self.get_element(locator).send_keys(text)
