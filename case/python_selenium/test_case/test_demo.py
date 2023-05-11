import pytest


from config.instantiate_driver import instantiate_driver
from pages.tool import Tool
from data.test_demo_data import DemoData


class TestDemo:
    def setup_method(self):
        self.driver = instantiate_driver()
        self.tool = Tool(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("text", ["selenium", "python"])
    def test_case1(self, text: str):
        data = DemoData(text)

        self.tool.open(data.url())
        self.tool.action_flow(data.actions())
        result = self.tool.get_attributes(data.results())
        assert (f"{text}" in result[0])     # 仅验证结果列表中第一个title是否有关键字
        self.driver.quit()
