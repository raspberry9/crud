import logging
from typing import Optional


def getLogger(name: Optional[str] = None) -> logging.Logger:  # pylint: disable=invalid-name
    return logging.getLogger(name)
