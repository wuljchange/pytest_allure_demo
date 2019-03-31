from utils.tools import TestNumberDemo, TestStringDemo
from utils.xls import gen_xls_data
import pytest
import allure


def pytest_generate_tests(metafunc):
    if 'data' in metafunc.fixturenames:
        argnames = 'data'
        argvalues = gen_xls_data(metafunc.cls.__name__, metafunc.function.__name__)
        metafunc.parametrize(argnames, argvalues, scope="function")


@allure.step('calculate')
@pytest.fixture(scope='class')
def calculate(request):
    cal_number = TestNumberDemo()
    return cal_number


@allure.step('replace string')
@pytest.fixture(scope='class')
def replace(request):
    rep_string = TestStringDemo()
    return rep_string
