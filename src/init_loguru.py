"""
    Loguru
    https://github.com/mysterious-ben/logutil

    Author:           @MarceloPalin
    Created:          2021-07-18
"""


import sys
from pathlib import Path
from typing import Optional, Union

from loguru import logger as _logger

PathType = Union[str, Path]
LevelType = Union[str, int]


def init_loguru(
    fmt: str = "{time:YYYY-MM-DDTHH:mm:ss.SSS!UTC-3}Z {name} {level}: {message}",
    level: Union[str, int] = "DEBUG",
    enqueue: bool = False,
    stream_on: bool = True,
    file_on: bool = True,
    file_fmt: Optional[str] = None,
    file_path: PathType = Path(__file__).absolute().parent / "logs" / "log.log",
    file_rotation: str = "20 MB",
    file_retention: int = 1,
    backtrace: bool = False,
    diagnose: bool = False,
):
    """Initialize loguru logging

    :param fmt: logging format
    :param level: logging level (stream and file handlers)
    :param enqueue: set true to make multiprocess / async safe
        always thread-safe
    :param stream_on: include stream logging handler
    :param file_on: include file logging handler
    :param file_fmt: file logging format (if None, fmt is used)
    :param pushover_fmt: pushover logging format (if None, fmt is used)
    :param file_path: log file path
    :param file_rotation: rotate log file when it reaches this size
    :param file_retention: keep <n> old log file
    """
    from loguru import logger as _logger

    _logger.remove()
    if stream_on:
        _logger.add(sys.stderr, format=fmt, level=level, enqueue=enqueue)

    if file_on:
        file_fmt = fmt if file_fmt is None else file_fmt
        _logger.add(
            file_path,
            format=file_fmt,
            level=level,
            enqueue=enqueue,
            rotation=file_rotation,
            retention=file_retention,
            backtrace=backtrace,
            diagnose=diagnose,
        )


def get_loguru_logger():
    return _logger
