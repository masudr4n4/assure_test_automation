import os
from py.path import local
import configparser
from utilities.custom_logger import customLogger as cl
import logging

project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
logger = cl(logging.INFO)


def get_config():
    config_file_Path = os.path.join(project_path, "config.ini")
    config_parser = configparser.RawConfigParser()
    config_parser.read(config_file_Path)
    return config_parser


config = get_config()
