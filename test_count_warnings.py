import pytest
from count_warnings import is_valid_aruguments
from count_warnings import get_warn_count_by_file
from count_warnings import get_warning_count
from count_warnings import is_build_promoted
from count_warnings import main

test_main_data = [
    {"data": ["count_warnings.py", "2log.txt", "1log.txt"],
        "exp_result": True},
    {"data": ["count_warnings.py", "1log.txt", "2log.txt"],
        "exp_result": False},
    
]
@pytest.mark.parametrize("ipd", test_main_data)
def test_main(ipd):
    retval = main(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


test_main_data_excp = [
    {"data": ["count_warnings.py", "1log.txt"],
        "exp_result":SystemExit}
]
@pytest.mark.parametrize("ipd", test_main_data_excp)
def test_main_data_excpection(ipd):
    with pytest.raises(ipd["exp_result"]):
        main(ipd["data"])

    

test_is_valid_aruguments_data = [
    {"data": ("vinay", "1log.txt", "2log.txt"), "exp_result": True},
    {"data": ("vinay", "1log.txt"), "exp_result": False},
    {"data": ("vinay"), "exp_result": False},
    {"data": ("vinay", "1log.txt", "2log.txt", "hggkj"), "exp_result": False},
    {"data": (" "), "exp_result": False},
]
@pytest.mark.parametrize("ipd", test_is_valid_aruguments_data)
def test_is_valid_aruguments(ipd):
    retval = is_valid_aruguments(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


test_get_warn_count_by_file_data = [
    {"data": "1log.txt", "exp_result": 4},
    {"data": "2log.txt", "exp_result": 5},
    {"data": "3log.txt", "exp_result": 0},
    {"data": " ", "exp_result": 0}
]
@pytest.mark.parametrize("ipd", test_get_warn_count_by_file_data)
def test_get_warn_count_by_file(ipd):
    retval = get_warn_count_by_file(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


test_get_warning_count_data = [
    {"data": ["warning", "is warning", "warning  warning"], "exp_result": 4},
    {"data": ["warning", "is the warning", "warning"], "exp_result": 3},
    {"data": [''], "exp_result": 4},
]
@pytest.mark.parametrize("ipd", test_get_warning_count_data)
def test_get_warning_count(ipd):
    retval = get_warning_count(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


test_is_build_promoted_data = [
    {"data": [['1log.txt', 4], ['2log.txt', 5]], "exp_result": -1},
    {"data": [['1log.txt', 5], ['2log.txt', 4]], "exp_result": 0},
]
@pytest.mark.parametrize("ipd", test_is_build_promoted_data)
def test_is_build_promoted(ipd):
    retval = is_build_promoted(ipd["data"])
    print(retval)
    assert retval == ipd["exp_result"]


test_is_build_promo_exce = [
    {"data": [['1log.txt'], ['2log.txt']], "exp_result": IndexError},
    {"data": [[], []], "exp_result": IndexError},
]
@pytest.mark.parametrize("ipd", test_is_build_promo_exce)
def test_is_build_promoted_exception(ipd):

    with pytest.raises(ipd["exp_result"]):
        is_build_promoted(ipd["data"])
