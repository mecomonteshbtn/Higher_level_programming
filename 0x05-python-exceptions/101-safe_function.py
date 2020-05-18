#!/usr/bin/python3


def safe_function(fct, *args):
    """
    executes a function safely and return the result of the function
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
