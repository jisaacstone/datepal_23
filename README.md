Find the nearest palindromic date to a given date

## Usage ##

command line:

		$ python -m datepal 1776
		1771

python:

		>>> from datepal import datepal
		>>> datepal.nearest_palindrome(1776)
		1771


## Testing ##

use the `runtests` shell script. If that doesn't work run `python setup.py test`
