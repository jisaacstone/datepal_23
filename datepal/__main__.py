import datepal
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {} DATE".format(sys.argv[0]))
    else:
        try:
            print(datepal.nearest_palindrome(sys.argv[1]))
        except (TypeError, ValueError) as e:
            print(e)
            print("usage: {} DATE".format(sys.argv[0]))
