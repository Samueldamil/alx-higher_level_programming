#!/usr/bin/python3
# Author - Edun Damilare

"""Print numbers from 0 - 9 in decimal and hexadecimal"""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
