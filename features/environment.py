from utilities.general import config, project_path
from utilities.driver import get_driver
from utilities.custom_logger import customLogger as cl
import allure
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


def after_step(context, step):
    if step.status.name == 'failed':
        if "allure_behave.formatter:AllureFormatter" in context._config.format:
            allure.attach(context.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    try:
        stdout = context.stdout_capture.getvalue()
        stderr = context.stderr_capture.getvalue()
        if stdout:
            allure.attach(stdout, name="stdout", attachment_type=allure.attachment_type.TEXT)
        if stderr:
            allure.attach(stderr, name="stderr", attachment_type=allure.attachment_type.TEXT)
    except:
        pass
    if scenario.status.name != 'passed':
        context.browser.execute_script("document.body.style.zoom = '0.7'")
        context.browser.save_screenshot(project_path.join("screenshots",
                                                          f"{context.scenario.name[:60]}...scn.png").strpath)
    context.browser.quit()
