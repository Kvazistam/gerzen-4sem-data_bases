import time
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class SimpleLog:
    """Кастомный простой логер, который пишет данные в файл logs.txt"""

    def __init__(self, logfile="Lab_3/logs.txt", level_filter=LogLevel.DEBUG):
        self.logfile = logfile
        self.level_filter = level_filter
        self.log_params = {}

    def get_time(self):
        date = datetime.fromtimestamp(time.time())
        return date
    def setLevel(self, log_level: LogLevel):
        self.log_params["log_level"] = log_level

    def set_module(self, module: str):
        self.log_params["module"] = module

    def logout(self):
        with open(self.logfile, "a") as fp:
            log = f"--{self.get_time()}--"
            for key in self.log_params.keys():
                log += f"--{key}:{self.log_params[key]}--"
            log += '\n'
            fp.write(log)

    # Функции ниже существуют для совместного использования с логером модуля logging
    def info(self, msg=None):
        if msg:
            self.log_params["msg"] = msg
        self.log_params["log_level"] = LogLevel.INFO
        self.logout()

    def debug(self, msg):
        if msg:
            self.log_params["msg"] = msg
        self.log_params["log_level"] = LogLevel.DEBUG

        self.logout()

    def warning(self, msg=None):
        if msg:
            self.log_params["msg"] = msg
        self.log_params["log_level"] = LogLevel.WARNING
        self.logout()

    def error(self, msg=None):
        if msg:
            self.log_params["msg"] = msg
        self.log_params["log_level"] = LogLevel.ERROR
        self.logout()

    def critical(self, msg=None):
        if msg:
            self.log_params["msg"] = msg

        self.log_params["log_level"] = LogLevel.CRITICAL
        self.logout()



