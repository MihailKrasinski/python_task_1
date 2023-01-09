from logging import config
import logging


DEFAULT_CONFIG_LOGGER = 'logger/logger_config.log'
APPLICATION_NAME = 'main'
logger = logging.getLogger(APPLICATION_NAME)


log_config = {
    "version": 1,
    "root": {
        "handlers": ["handler_debug"],
        "level": "DEBUG"
    },
    "handlers": {
        "handler_debug": {
            "class": "logging.FileHandler",
            "filename": "data/out/debug.log",
            "level": "DEBUG",
            "formatter": "formatter_complex"
        }
    },
    "formatters": {
        "formatter_complex": {
            "class": "logging.Formatter",
            "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : "
                      "%(lineno)d : (Process Details : (%(process)d, %(processName)s), "
                      "Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
            "datefmt": "%d-%m-%Y %I:%M:%S"
        }
    },
    "loggers": {
        "main": {
            "level": "DEBUG",
            "handlers": ["handler_debug"],
            "propagate": "no"
        }
    }
}

config.dictConfig(log_config)




