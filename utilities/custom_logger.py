import inspect
import logging


def customLogger(logLevel=logging.INFO, logger=logging.getLogger(__name__)):
    # loggerName = inspect.stack()[1][3]
    logger.setLevel(logLevel)
    fileHandler = logging.FileHandler('test_automation.log', mode='a')
    fileHandler.setLevel(logLevel)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger