#!/usr/bin/python3
"""
Module that validates UTF-8
"""


def validUTF8(data):
    """
    Essentially its converting the data to
    hexadecimal. Then from hexadecimal to bytes
    after modifying it. From bytes its validated
    against UTF-8
    Args:
        data: list of integers
    Return:
        boolean value. True if valid False if not
    """
    try:
        bytes.fromhex(''.join(hex(bytez)[2:].zfill(4)
                      for bytez in data)).decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
