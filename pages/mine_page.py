from core.base_page import BasePage
from playwright.sync_api import expect

class MinePage(BasePage):

    def open_company(self, company_name):
        self.page.get_by_text(company_name).click()

    def add_mine(self, data):
        self.page.get_by_role("button", name="Add Mine").click()
        self.page.get_by_role("textbox", name="Enter MSHA Mine Name").fill(data["name"])
        self.page.get_by_text(data["name"]).click()
        self.type("input[name='addressLine1']", data["address"])
        self.type("input[name='zipCode']", data["zip"])

        self.page.get_by_title("Click to add new mine").click()
        self.page.get_by_role("button", name="Yes").click()

        expect(self.page.get_by_text("Mine created successfully")).to_be_visible()
