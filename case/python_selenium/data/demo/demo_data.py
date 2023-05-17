class DemoData:
    def url(self):
        return "https://www.sogou.com"
    
    def actions(self, party_name: str):
        return {
            "contacts_click" : "a#menu_contacts",
            "add_dropdown" : "div.member_colLeft a.member_colLeft_top_addBtnWrap@ul.js_create_dropdown_container@添加部门",
            "party_name_input" : f"input[name='name']@{party_name}",
            "select_party_dropdown" : "a.js_toggle_party_list@div.js_party_list_container@碎片计划",
            "submit_click": "a[d_ck='submit']"
        }

