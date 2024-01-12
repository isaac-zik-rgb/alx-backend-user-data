#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for i in fields:
        return re.sub(i + "=.*?" + separator,
                      i + "=" + redaction + separator, message)
