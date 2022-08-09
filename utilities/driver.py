from utilities.general import project_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


def get_driver(context, name):
    driver_path = project_path.strpath+"\\utilities\\chromedriver.exe"
    s = Service(executable_path=driver_path)
    name = name.lower()
    headless = context.config.userdata.get("headless", "false").lower()
    if name == 'chrome':
        chrome_options = Options()
        # chrome_options.page_load_strategy = 'eager'
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument("--log-level=OFF")
        if headless == "true":
            chrome_options.add_argument("--headless")
        # context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
        #                                    chrome_options=chrome_options)
        context.browser = webdriver.Chrome(service=s, options=chrome_options)
    elif name == 'firefox':
        if headless == "true":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
        context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise KeyError('This browser is not supported by this automation script at this time')
    context.browser.set_page_load_timeout(time_to_wait=100)
    context.browser.set_script_timeout(1000)
    context.browser.set_window_size(1920, 1080)
    context.browser.maximize_window()
    sleep(1)
    return context.browser