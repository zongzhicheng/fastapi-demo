# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 日志配置
"""

import logging.config
import os
from apps.core.config import Configs

LOG_PATH = os.path.join(Configs.application.BASE_DIR, Configs.application.LOG_DIR)
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # format 配置
    'formatters': {
        'simple': {
            'format': '%(asctime)s |%(levelname)s| |%(module)s:%(funcName)s:%(lineno)d| - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # Handler 配置
    'handlers': {
        'common': {
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/common.log',
            'formatter': 'simple',
            'level': 'INFO'
        },
        'back_end_with_algorithm': {
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/back_end_with_algorithm.log',
            'formatter': 'simple',
            'level': 'INFO'
        }
    },
    # Logger 配置
    'loggers': {
        'back_end_with_algorithm': {
            'handlers': ['back_end_with_algorithm'],
            'propagate': False,
            'level': 'INFO'
        },
        'common': {
            'handlers': ['common'],
            'propagate': False,
            'level': 'INFO'
        }
    }
}

# 配置 logger 日志
# DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.config.dictConfig(LOGGING)
back_end_with_algorithm_logger = logging.getLogger("back_end_with_algorithm")
common_logger = logging.getLogger("common")

if __name__ == '__main__':
    back_end_with_algorithm_logger.info("back_end_with_algorithm_logger test")
    common_logger.info("common_logger test")
