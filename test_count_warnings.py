"""TO import pytest module """
import pytest
from count_warnings import is_valid_aruguments
from count_warnings import get_warn_count_by_file
from count_warnings import get_warning_count
from count_warnings import is_build_promoted
from count_warnings import main

TEST_MAIN_DATA = [
        {"data": ["count_warnings.py", "2log.txt", "1log.txt"],
         "exp_result": True},
        {"data": ["count_warnings.py", "1log.txt", "2log.txt"],
         "exp_result": False}
        ]


@pytest.mark.parametrize("ipd", TEST_MAIN_DATA)
def test_main(ipd):
    ''' main function to print program status '''
    retval = main(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


TEST_MAIN_DATA_EXCP = [
        {"data": ["count_warnings.py", "1log.txt"],
         "exp_result":SystemExit}
        ]


@pytest.mark.parametrize("ipd", TEST_MAIN_DATA_EXCP)
def test_main_data_excpection(ipd):
    """ main data exceptions function block """
    with pytest.raises(ipd["exp_result"]):
        main(ipd["data"])


TEST_IS_VALID_ARUGUMENTS_DATA = [
        {"data": ["vinay", "1log.txt", "2log.txt"], "exp_result": True},
        {"data": ["vinay", "1log.txt"], "exp_result": False},
        {"data": ["vinay"], "exp_result": False},
        {"data": ["vinay", "1log.txt", "2log.txt", "hggkj"],
         "exp_result": True},
        {"data": [" "], "exp_result": False}
        ]


@pytest.mark.parametrize("ipd", TEST_IS_VALID_ARUGUMENTS_DATA)
def test_is_valid_aruguments(ipd):
    """ function to get given arguments are valid or not valid """
    retval = is_valid_aruguments(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


TEST_GET_WARN_COUNT_BY_FILE_DATA = [
        {"data": "1log.txt", "exp_result": 4},
        {"data": "2log.txt", "exp_result": 5},
        {"data": "3log.txt", "exp_result": 0},
        {"data": " ", "exp_result": 0}
        ]


@pytest.mark.parametrize("ipd", TEST_GET_WARN_COUNT_BY_FILE_DATA)
def test_get_warn_count_by_file(ipd):
    """ function to get number read data from the given file """
    retval = get_warn_count_by_file(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


TEST_GET_WARNING_COUNT_DATA = [
        {"data": ["warning", "is warning", "warning  warning"],
         "exp_result": 3},
        {"data": ["warning", "is the warning", "warning"], "exp_result": 3},
        {"data": [''], "exp_result": 0}
        ]


@pytest.mark.parametrize("ipd", TEST_GET_WARNING_COUNT_DATA)
def test_get_warning_count(ipd):
    """function to get warning count"""
    retval = get_warning_count(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


TEST_IS_BUILD_PROMOTED_DATA = [
        {"data": [['1log.txt', 4], ['2log.txt', 5]], "exp_result": -1},
        {"data": [['1log.txt', 5], ['2log.txt', 4]], "exp_result": 0}
        ]


@pytest.mark.parametrize("ipd", TEST_IS_BUILD_PROMOTED_DATA)
def test_is_build_promoted(ipd):
    """ function to get status of valid data """
    retval = is_build_promoted(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


TEST_IS_BUILD_PROMO_EXCE = [
        {"data": [['1log.txt'], ['2log.txt']], "exp_result": IndexError},
        {"data": [[], []], "exp_result": IndexError}
        ]


@pytest.mark.parametrize("ipd", TEST_IS_BUILD_PROMO_EXCE)
def test_is_build_promoted_exception(ipd):
    """ function to get status of non-valid data """
    with pytest.raises(ipd["exp_result"]):
        is_build_promoted(ipd["data"])
