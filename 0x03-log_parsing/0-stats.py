#!/usr/bin/python3
"""this script parse results based on stats"""
import sys
import re


counter = 0
file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
pattern = re.compile(
    r'''
    ^(\d+\.\d+\.\d+\.\d+)          # IP Address
    \s-\s\[(.+)\]                   # Date
    \s"GET\s/projects/260\sHTTP/1.1" # Request
    \s(\d+)                          # Status Code
    \s(\d+)$                         # File Size
    ''',
    re.VERBOSE
)

while True:
    try:
        line = sys.stdin.readline()
        match = pattern.match(line)
        if match:
            _, _, s_code, f_size = match.groups()
            file_size += int(f_size)
            if int(s_code) in status_codes:
                status_codes[int(s_code)] += 1
            counter += 1
        if (counter % 10 == 0):
            print("File size:{}".format(file_size))
            for key, value in status_codes.items():
                if (value):
                    print("{}: {}".format(key, value))
    except KeyboardInterrupt:
        print("File size:{}".format(file_size))
        for key, value in status_codes.items():
            if (value):
                print("{}: {}".format(key, value))
        break
