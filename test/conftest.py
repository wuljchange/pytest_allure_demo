from utils.tools import TestNumberDemo, TestStringDemo
import pytest
import allure


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
