#!/usr/bin/python3
"""
Module that validates UTF-8
"""


def validUTF8(data):
    """
    Go through each byte in the dataset.
    Then confirm if it follows the UTF-8 rule.
    Returns:
        bool: True if valid False if not
    """
    num_bytes = 0

    for byte in data:
        # Maksure the 8 least significant bits are used
        byte = byte & 0xFF
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
