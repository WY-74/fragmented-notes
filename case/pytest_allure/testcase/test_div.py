"""
有效等价类
    1. -99<=x<=99 and -99<=y<=99
    2. 整数或浮点数
无效等价类
    3. x<-99 or x >99 or y<-99 or y>99
    4. 非整数或浮点数
    5. 除数为0
边界值
    5. -99, 99
用例:
    x=-99, y=99
    x=55.5, y=55.5

    x=-99.1, y=99
    x=-99, y=99.1
    x="a", y="b"
    x=10, y=0
"""

import pytest
import allure
import logging
import yaml


class TestDiv:
    @staticmethod
    def get_data(tag):
        with open("data/data_div.yaml", "r") as f:
            return yaml.safe_load(f)[tag]

    @pytest.mark.valid
    @allure.title("有效等价类+边界值: {x}, {y}")
    @pytest.mark.parametrize("x, y, expected", get_data("valid"))
    def test_01(self, x, y, expected, calculator):
        logging.info(f"有效等价类{x}, {y}")
        assert calculator.div(x, y) == expected
        allure.dynamic.title("此数据组测试通过!")

    @pytest.mark.no_valid
    @allure.title("有效等价类+边界值: {x}, {y}")
    @pytest.mark.parametrize("x, y, expected", get_data("no_valid"))
    def test_02(self, x, y, expected, calculator):
        logging.info(f"无效等价类{x}, {y}")
        assert calculator.div(x, y) == expected
        allure.dynamic.title("此数据组测试通过!")
