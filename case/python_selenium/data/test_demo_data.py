class DemoData:
    def __init__(self, text: str):
        self.text = text

    def url(self):
        return "https://ceshiren.com/"

    def actions(self):
        return {
            "search_click": "button#search-button",
            "advanced-search_click": "a.show-advanced-search",
            "search_input": f"input.full-page-search@{self.text}",
            "submit_click": "button.search-cta",
        }

    def results(self):
        return "span.topic-title@text"
