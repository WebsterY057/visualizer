"""
日志配置 - 统一日志输出格式和级别
"""

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = '/tmp'
LOG_FILE = os.path.join(LOG_DIR, 'visualizer.log')
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
MAX_BYTES = 10 * 1024 * 1024  # 10MB
BACKUP_COUNT = 3


def setup_logger(name='visualizer'):
    """创建并返回配置好的logger"""
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(LOG_FORMAT)

    # 文件Handler - 滚动日志
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)

    # 控制台Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 全局logger实例
logger = setup_logger()
