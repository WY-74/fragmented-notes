import time
from typing import Dict

from pages.base_pages import BasePages
from utils.decorator import save_cookies, load_cookies



class DemoPages(BasePages):
    @save_cookies
    def login(self):
        self.open("https://work.weixin.qq.com/wework_admin")
        self.must_after_cilck("a.index_top_operation_loginBtn", "span.ww_loginImg_LoginLogo")
        time.sleep(30)


    @load_cookies
    def navigate(self):
        self.open("https://work.weixin.qq.com/wework_admin")
        self.must_after_cilck("a.index_top_operation_loginBtn", "span.frame_nav_item_title")

    def new_party(self, actions: Dict[str, str]):
        self.action_flow(actions)
    
    def verify_new_party(self, party_name: str):
        assert self.get_attributes("text", "ul.jstree-children ul.jstree-children li:last-child a")[0] == party_name
