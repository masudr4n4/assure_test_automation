from enum import Enum
from retry import retry
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from utilities.general import config


class BasePage():
    WAIT = 40

    def __init__(self, context):
        self.driver = context.browser
        self.context = context

    def __get_by(self, locator_with_strategy):
        """
        Get and return By instance based on the locator strategy
        :param locator_with_strategy: Element locator strategy
        :return: By instance of the element
        """
        if "@@" not in locator_with_strategy:
            locator_with_strategy = Strategy.ID.value + "@@" + locator_with_strategy
        strategy_and_locator = str(locator_with_strategy).split("@@")
        strategy = strategy_and_locator[0]
        locator = strategy_and_locator[1]
        by = None
        if strategy == Strategy.XPATH.value:
            by = (By.XPATH, locator)
        elif strategy == Strategy.ID.value:
            by = (By.ID, locator)
        elif strategy == Strategy.CSS.value:
            by = (By.CSS_SELECTOR, locator)
        elif strategy == Strategy.TAGNAME.value:
            by = (By.TAG_NAME, locator)
        elif strategy == Strategy.NAME.value:
            by = (By.NAME, locator)
        return by

    def click_backspace(self, locator, times=3):
        ele = self.find_element(locator)
        for i in range(times):
            ele.send_keys(Keys.BACK_SPACE)

    def open(self, url):
        self.driver.get(url)
        self.wait_for_page_loaded()

    def open_homepage(self):
        self.driver.get(config.get("URL", 'url'))

    def find_element(self, locator):
        """
        Find and return the list of webelements based on the given locator value
        :param locator: Element locator strategy
        :return: list of the elements
        """
        return self.driver.find_element(
            *self.__get_by(locator_with_strategy=locator))

    def find_elements(self, locator):
        """
        Find and return the list of webelements based on the given locator value
        :param locator: Element locator strategy
        :return: list of the elements
        """
        return self.driver.find_elements(
            *self.__get_by(locator_with_strategy=locator))

    @retry(StaleElementReferenceException, tries=1)
    def click(self, locator):
        """
        Clicks the given element
        :param locator: Element locator strategy
        :return: element
        """
        element = None
        if isinstance(locator, str):
            element = self.find_element(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            try:
                element.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("""
                            var element = arguments[0];
                            element.click();
                            """, element)
        else:
            raise Exception("Could not click on locator " + element)

    def move_and_click(self, locator):
        """
        Move and click to the given element using
        selenium action class
        :param locator: Element locator strategy
        :return: element
        """
        self.wait_till_element_is_visible(locator)
        element = self.find_element(locator)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
        except Exception as e:
            raise Exception(
                "Could Not click locator {} due to {}".format(
                    element, e))
        return element

    def hover(self, locator, wait_seconds=2):
        """
        Hover over the element
        :param locator: locator
        :param wait_seconds: time to wait
        :return:
        """
        element = self.find_element(locator)
        action_obj = ActionChains(self.driver)
        action_obj.move_to_element(element)
        action_obj.perform()
        return element

    def wait_till_element_is_visible(self, locator, timeout=WAIT):
        """
        WebDriver Explicit wait till element is not visible, once visible wait will over
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """

        try:
            element = WebDriverWait(
                self.browser,
                timeout,
                ignored_exceptions=NoSuchElementException).until(
                EC.visibility_of_element_located(
                    self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_invisible(self, locator, timeout=WAIT):
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency=2). \
                until(
                EC.invisibility_of_element_located(self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_clickable(self, locator, timeout=WAIT):
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency=2).until(EC.element_to_be_clickable(
                self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def send_keys(self, locator, *keys):
        """
        send keys to locator
        :param locator: element
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(*(keys))
        except Exception as e:
            raise e

    def wait_for_element_to_be_staleness(self, locator, timeout=10):
        element = self.find_element(locator)
        WebDriverWait(self.driver, timeout).until(staleness_of(element))

    def wait_for_page_loaded(self, timeout=WAIT):
        WebDriverWait(self.driver, timeout).until(PageLoaded())

    def wait_till_element_is_present(self, locator, timeout=WAIT):
        """
        WebDriver Explicit wait till element is present
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        try:
            element = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=2,
                ignored_exceptions=NoSuchElementException).until(
                EC.presence_of_element_located(
                    self.__get_by(locator)
                ))
            return element
        except Exception as e:
            raise e

    def wait_till_url_contains(self, url_substring, timeout=WAIT):
        """
        WebDriver Explicit wait till the current url contains a case-sensitive substring
        :param url_substring: url_substring to be checked
        :param timeout: waiting time
        :return: True when the url matches, TimeoutException otherwise
        """
        try:
            return WebDriverWait(self.driver, timeout). \
                until(EC.url_contains(url_substring))
        except Exception:
            raise TimeoutException(
                f"URL does not contain \"{url_substring}\" substring") from Exception

    def wait_till_element_is_visible(self, locator, timeout=WAIT):
        """
        WebDriver Explicit wait till element is not visible, once visible wait will over
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """

        try:
            element = WebDriverWait(
                self.driver,
                timeout,
                ignored_exceptions=NoSuchElementException).until(
                EC.visibility_of_element_located(
                    self.__get_by(locator)))
            return element
        except Exception as e:
            raise e


class PageLoaded:
    def __call__(self, dr):
        ready = dr.execute_script(
            "return document.readyState=='complete';"
        )
        if ready:
            return True
        else:
            return False


class Strategy(Enum):
    """
    Locator Strategy Constants
    """
    XPATH = "xpath"
    ID = "id"
    CSS = "css"
    TAGNAME = "tag name"
    NAME = "name"
