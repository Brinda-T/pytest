""" This file is to test count_warning functions """

from count_warnings import main


def test_main():
    """ test function for of main """

    test_data = ["count_warnings.py", "1log.txt", "2log.txt"]
    retval = main(test_data)
    print(retval)
