from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def type(self, locator, value):
        self.page.locator(locator).fill(value)

    def wait_visible(self, locator, timeout=10000):
        expect(self.page.locator(locator)).to_be_visible(timeout=timeout)

    def select(self, locator, value):
        self.page.locator(locator).select_option(value)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def scroll_into_view(self, locator):
        self.page.locator(locator).scroll_into_view_if_needed()

    def wait_for_table_load(self):
        self.page.wait_for_selector("table", timeout=20000)
