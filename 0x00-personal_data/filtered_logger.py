#!/usr/bin/env python3
""" module filtered_logger.py """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscates specified fields in the log message."""
    for field in fields:
        message = re.sub(fr'{field}=(.*?){re.escape(separator)}',
                         f'{field}={redaction}{separator}', message)
    return message
