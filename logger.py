import logging
import sys
from logging import StreamHandler, Formatter

forms = ('[%(asctime)s][%(levelname)s]:%(message)s')

def get_console_handler():
    console_handler = StreamHandler(sys.stdout)
    console_handler.setFormatter(Formatter(forms))
    return console_handler

def getLogger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    return logger
