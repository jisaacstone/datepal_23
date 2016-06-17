# coding: utf8
import math
import sys

# One line makes this py2&3 interoperable
string_type = basestring if sys.version_info[0] == 2 else str


def nearest_palindrome(date):
    """Return the nearest palindromic date to `date`

    `date` can be a string or an integer. The return type will match the input
    type.

    If two palindromes are eqidistant then one of the two will be chosen.

    If a negative value is povided then `0` will be returned, as it is the
    nearest palandromic number to any negative value.
    """

    if isinstance(date, string_type):
        if not date.isdigit():
            if date[0] == "-" and date[1:].isdigit():
                return "0"

            raise ValueError("Date must be numeric")

        # Pretending str/unicode/bytes are interchangable -_-
        return str(nearest_palindrome(int(date)))

    if isinstance(date, float):
        # explicitly not supporint this - code handels it well enough
        raise TypeError("floating-point dates are not supported")

    if date < 0:
        return 0

    if palindrome(date):
        return date

    # Calculation is imprecise, aka 'good enough'
    if order_of_magnitude(date) > (
            order_of_magnitude(sys.getrecursionlimit()) * 2):
        raise ValueError("Date is too far in the future ...")

    return _nearest_palindrome(date, 1)


def _nearest_palindrome(date, offset):
    # Naïeve solution - make more efficienet if/when necessary
    if palindrome(date - offset):
        return date - offset
    elif palindrome(date + offset):
        return date + offset
    return _nearest_palindrome(date, offset + 1)


def palindrome(dateint):
    datestr = str(dateint)
    return datestr == datestr[::-1]


def order_of_magnitude(num):
    return int(math.log10(num))
