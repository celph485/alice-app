import os
import platform
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import date
from typing import Final


USER_ID: Final = ''
CLIENT_ID: Final = ''
PASSWORD: Final = ''
TXN_PASSWD: Final = ''
TWO_FA_CODE: Final = ''
CLIENT_SECRET: Final = ''
CALLBACK_URL: Final = 'https://ant.aliceblueonline.com/plugin/callback'
AUTH_URL: Final = 'https://ant.aliceblueonline.com/oauth2/auth'
ACCESS_TOKEN_URL: Final = 'https://ant.aliceblueonline.com/oauth2/token'

DIR_SEP: Final = os.path.sep
USER_DIR: Final = str(Path.home())
LOG_DIR: Final = f'{USER_DIR}{DIR_SEP}alice{DIR_SEP}logs{DIR_SEP}'
DEF_DATE_FORMAT: Final = '%Y-%m-%d'
DEF_DATETIME_FORMAT: Final = '%Y-%m-%d %H:%M:%S'


def __log_file_path():
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    curr_date_str = date.today().strftime(DEF_DATE_FORMAT)
    file_path = f'{LOG_DIR}alice-{curr_date_str}.log'
    return file_path


def __get_file_handler():
    max_file_size_in_bytes = 10_485_760
    max_file_backup_per_day = 2000
    file_path = __log_file_path()
    file_fmt = '%(asctime)s :: %(levelname)-8s :: %(filename)-18s:%(lineno)3d :: %(message)s'
    handler = RotatingFileHandler(file_path,
                                  maxBytes=max_file_size_in_bytes,
                                  backupCount=max_file_backup_per_day,
                                  delay=True)
    handler.setFormatter(logging.Formatter(file_fmt))
    return handler


def __get_console_handler():
    console_fmt = '%(levelname)-8s :: %(filename)-18s:%(lineno)3d :: %(message)s'
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(console_fmt))
    return handler


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    log.addHandler(__get_file_handler())
    log.addHandler(__get_console_handler())
    return log
