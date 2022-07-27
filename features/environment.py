from utilities.general import config, project_path
from utilities.driver import get_driver
from utilities.custom_logger import customLogger as cl

import logging
import os


def before_all(context):
    print('Thank you for running the automation suite at Assure')
    if not os.path.isdir(project_path.join("screenshots").strpath):
        os.mkdir(project_path.join("screenshots").strpath)
    screenshots_list = os.listdir('screenshots')
    if len(screenshots_list) > 0:
        for file in screenshots_list:
            os.remove('screenshots/' + file)


def before_scenario(context, scenario):
    log = cl(logger=logging.getLogger("environment"))
    default_browser = config.get("BROWSER", 'default_browser')
    browser = context.config.userdata.get("browser", default_browser)
    context.browser = get_driver(context, browser)
    # log.info(f"Opened {browser} browser")


def after_scenario(context, scenario):
    if scenario.status.name != 'passed':
        context.browser.execute_script("document.body.style.zoom = '0.7'")
        context.browser.save_screenshot(project_path.join("screenshots",
                                                          f"{context.scenario.name[:60]}...scn.png").strpath)
    context.browser.quit()
