import time
from data.demo.demo_data import DemoData
from pages.demo.demo_pages import DemoPages
from testcases.base_test import BaseTest
from utils.decorator import exception_capture

class TestDemo(BaseTest):
    def setup_class(self):
        super().setup_class(self)
        self.data = DemoData()
        self.page = DemoPages(self.driver)
        self.page.login()

    @exception_capture
    def test_demo_case1(self):
        self.page.navigate()
        self.page.new_party(self.data.actions("this is new one2"))
        time.sleep(5)
        self.page.verify_new_party("this is new one2")

