#!/usr/bin/python3
"""
Stat logger
This module reads from stdin
"""

import re
import sys

ip_regex = re.compile(
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP Address
    r' - \[(?P<date>.*?)\]'  # Date
    r' "(?P<request>.*?)"'  # Request
    r'(?P<status_code>\d{3})'  # Status Code
    r'(?P<file_size>\d+)'  # File Size
)

stat_code_list = {200: 0,
                  301: 0,
                  400: 0,
                  401: 0,
                  403: 0,
                  404: 0,
                  405: 0,
                  500: 0}


def dump_metrics(size):
    """This function just prints metrics"""
    print(f"File size: {size}")
    for stat_code in sorted(stat_code_list.keys()):
        occurence = stat_code_list[stat_code]
        if occurence > 0:
            print(f"{stat_code}: {occurence}")


def runApp():
    """Run app"""
    counter = 0
    total_size = 0
    try:

        for line in sys.stdin:
            ip_list_match = ip_regex.match(line)

            if ip_list_match:
                try:
                    status_code = int(ip_list_match.group("status_code"))
                    file_size = int(ip_list_match.group("file_size"))
                except (ValueError, IndexError):
                    continue
                total_size += file_size
                stat_code_list[status_code] += 1
                counter += 1
            if counter % 10 == 0:
                dump_metrics(total_size)
    except (KeyboardInterrupt, EOFError):
        dump_metrics(total_size)


if __name__ == '__main__':
    runApp()
