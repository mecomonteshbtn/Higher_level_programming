#!/usr/bin/python3


def safe_print_integer_err(value):
    """
    prints an integer followed bya  new line and Returns
    True if value is correctly printed, or False in otherwise
    and prints sterr precede by Exception:
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    else:
        return True
