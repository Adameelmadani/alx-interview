#!/usr/bin/python3
"""
This is our python module
"""
import sys
"""
This is sys module
"""


i = 0
total_size = 0
status_codes = {200: 0,
                301: 0,
                400: 0,
                401: 0,
                403: 0,
                404: 0,
                405: 0,
                500: 0}


def print_func(t_size, s_codes):
    """
    This is print function
    """
    print("File size:", t_size)
    for key, value in s_codes.items():
        if value != 0:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        i = i + 1
        status = ""
        fsize = ""
        try:
            ln = line.strip()
            split1 = ln.split(" - ", maxsplit=1)
            split2 = split1[1].split("] ", maxsplit=1)
            split3 = split2[1].split("\"GET /projects/260 HTTP/1.1\" ")
            final_split = split3[1].split(" ", maxsplit=1)
            status = int(final_split[0])
            fsize = int(final_split[1])
        except Exception as e:
            continue
        total_size = total_size + fsize
        if status in status_codes:
            status_codes[status] = status_codes[status] + 1
        if i == 10:
            i = 0
            print_func(total_size, status_codes)
except KeyboardInterrupt:
    print_func(total_size, status_codes)
    raise
