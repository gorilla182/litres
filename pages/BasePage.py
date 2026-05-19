from playwright.sync_api import Page

class BasePage:

    url = ''
    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def reload(self):
        self.page.reload()

    def get_current_url(self):
        return self.page.url