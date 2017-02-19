# stelligent_programming_exercise
Programming Exercise written in Python based on directions here: https://docs.google.com/document/d/1ijlkx1H2DJGYBc5L04r-JEpnwxmBmYjRgXz74DOcuxM

## Notes and Assumptions
- All test files were generated using a random text generator (http://randomtextgenerator.com/)
- The search_locality.py script can be used to interpret any single term or phrases, including punctuation and casing, but the items inside will be altered to remove their punctuation and casing for an easier search (i.e. Dr. becomes Dr and Hello becomes hello).  This of course goes for both the search terms and the text being checked against to best find a match.
- Uses python 2.7
- Will only look for .txt files in a directory.  Will not check subdirectories of that directory and will ignore all other file types/extensions.

## Usage
The search_locality.py file has a built-in argument parser with help message to explain how to use it.  To elaborate on that:
```
python search_locality.py [-h] term_1 term_2 [context] [dir_name]
```
- The -h flag will bring up a detailed help menu, otherwise do not use this flag to avoid this message from appearing as it overrides other parameters
- term_1 and term_2 are required items, these are the search terms to be used.  For phrases, it is best to double-quote the terms.
- context defaults to 1, and can be any integer.  This is the number of words in between each term to check, so it will find if the two terms exist this number of words or less apart from each other.
- dir_name defaults to current working directory.  Otherwise, use this to point at the directory containing all .txt files you wish to check against.

## Examples
*Note: There are test files that exist in the tests directory and tests/more_tests directory to run against if so desired.  The .txt files will be checked against, and any other types or subdirectories, like tests/file3.sh, will be ignored.*

### Run against local working directory with context of 1 (Minimal parameters)
For singular word terms
```
python search_locality.py hello world
```
For phrases
```
python search_locality.py "hello world" "how are you"
```

### Run against local working directory with context of 8
For singular word terms
```
python search_locality.py hello world 8
```
For phrases
```
python search_locality.py "hello world" "how are you" 8
```

### Run against specific directory with context of 20
For singular word terms
```
python search_locality.py hello world 20 tests
```
For phrases
```
python search_locality.py "hello world" "how are you" 20 tests
```

## To execute tests, run the following.

Ensure test runners are installed:
```
pip install pytest pytest-cov
```
Run tests w/coverage (from tests directory):
```
py.test --cov-report term-missing --cov test_search.py
```
