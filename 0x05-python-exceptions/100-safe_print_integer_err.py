#!/usr/bin/python3


def safe_print_integer_err(value):
    """
    prints an integer followed bya  new line and Returns
    True if value is correctly printed, or False in otherwise
    and prints sterr precede by Exception:
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e))
        return False
