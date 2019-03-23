import pytest
import allure

from py_case.data import DATA, DATA2, DATA3


@allure.feature('test_calculate_number')
@pytest.mark.calculate
class TestCalculate:
    @allure.story('test_add')
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.jira.com")
    @pytest.mark.parametrize('cid, num1, num2, excepted', DATA)
    def test_add(self, calculate, cid, num1, num2, excepted):
        real = calculate.add(self, num1, num2)
        assert real == excepted

    @allure.story('test_sub')
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.jira.com")
    @pytest.mark.parametrize('cid, num1, num2, excepted', DATA2)
    def test_sub(self, calculate, cid, num1, num2, excepted):
        real = calculate.sub(self, num1, num2)
        assert real == excepted


@allure.feature('test_replace_string')
@pytest.mark.replace
class TestReplace:
    @allure.story('test_replace_all')
    @allure.severity('blocker')
    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.jira.com")
    @pytest.mark.parametrize('cid, raw, pattern, new, excepted', DATA3)
    def test_replace(self, replace, cid, raw, pattern, new, excepted):
        real = replace.replace_all(self, raw, pattern, new)
        assert real == excepted
