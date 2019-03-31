import pytest
import allure

from py_case.data import DATA, DATA2, DATA3


# 标记功能模块的关键字 calculate
@pytest.mark.calculate
class TestCalculate:
    # feature表示主要功能模块
    @allure.feature('test_calculate_number')
    # story表示主要功能模块下的分支功能
    @allure.story('test_add')
    # 参数化case
    @pytest.mark.parametrize('cid, num1, num2, excepted', DATA)
    def test_add(self, calculate, cid, num1, num2, excepted):
        real = calculate.add(self, num1, num2)
        assert real == excepted

    @allure.feature('test_calculate_number')
    @allure.story('test_sub')
    @pytest.mark.parametrize('cid, num1, num2, excepted', DATA2)
    def test_sub(self, calculate, cid, num1, num2, excepted):
        real = calculate.sub(self, num1, num2)
        assert real == excepted


@pytest.mark.replace
class TestReplace:
    @allure.feature('test_replace_string')
    @allure.story('test_replace_all')
    @pytest.mark.parametrize('cid, raw, pattern, new, excepted', DATA3)
    def test_replace(self, replace, cid, raw, pattern, new, excepted):
        real = replace.replace_all(self, raw, pattern, new)
        assert real == excepted


# 测试xls文件的case
@pytest.mark.xls
class TestXls:
    @allure.feature('test_xls_case')
    @allure.story('test_xls_add')
    def test_add(self, calculate, data):
        real = calculate.add(data['num1'], data['num2'])
        assert real == data['expected']

    @allure.feature('test_xls_case')
    @allure.story('test_xls_sub')
    def test_sub(self, calculate, data):
        real = calculate.sub(data['num1'], data['num2'])
        assert real == data['expected']
