import os
from py.path import local
import configparser
from utilities.custom_logger import customLogger as cl
import logging
import random,string
project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
logger = cl(logging.INFO)


def get_config():
    config_file_Path = os.path.join(project_path, "config.ini")
    config_parser = configparser.RawConfigParser()
    config_parser.read(config_file_Path)
    return config_parser


config = get_config()


def get_random_email():
    s = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    email = "ra" + s + "@assure.com"
    return email

def get_random_email_for_org():
    s = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    email = "org" + s + "@assure.com"
    return email