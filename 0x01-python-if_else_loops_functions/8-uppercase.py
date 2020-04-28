#!/usr/bin/python3


def uppercase(str):
    for c in str:
        char = ord(c)
        if char >= 97 and char <= 122:
            char -= 32
        print("{:c}".format(char), end="")
    print()
