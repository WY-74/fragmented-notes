import pytest
import allure
import logging
import yaml


class TestAdd:
    @staticmethod
    def get_data(tag):
        with open("data/data_add.yaml", "r") as f:
            return yaml.safe_load(f)[tag]

    @pytest.mark.valid
    @allure.title("有效等价类+边界值: {x}, {y}")
    @pytest.mark.parametrize("x, y, expected", get_data("valid"))
    def test_01(self, x, y, expected, calculator):
        logging.info(f"有效等价类{x}, {y}")
        assert calculator.add(x, y) == expected
        allure.dynamic.title("此数据组测试通过!")

    @pytest.mark.no_valid
    @allure.title("无效等价类+边界值: {x}, {y}")
    @pytest.mark.parametrize("x, y, expected", get_data("no_valid"))
    def test_02(self, x, y, expected, calculator):
        logging.info(f"无效等价类{x}, {y}")
        assert calculator.add(x, y) == expected
        allure.dynamic.title("此数据组测试通过!")
