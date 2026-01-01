from datetime import date, timedelta
from playwright.sync_api import expect
from locators.date_filter_locators import DateFilterLocators







class DateFilterPage:

    def __init__(self, page):
        self.page = page

    def open_date_picker(self):
        input_box = self.page.locator(DateFilterLocators.DATE_RANGE_INPUT)
        expect(input_box).to_be_visible(timeout=15000)
        input_box.click()

        popup = self.page.locator(DateFilterLocators.DATE_PICKER_POPUP)
        expect(popup).to_be_visible(timeout=15000)

    def select_predefined_option(self, option_text):
        option = DateFilterLocators.PREDEFINED_OPTION.format(option=option_text)
        self.page.locator(option).click()

    def get_selected_date_range(self):
        return self.page.locator(
            DateFilterLocators.DATE_RANGE_INPUT
        ).input_value()

    # ---------- Expected Date Calculations ----------

    def expected_today_range(self):
        today = date.today().strftime("%b %d, %Y")
        return f"{today} - {today}"

    def expected_yesterday_range(self):
        d = date.today() - timedelta(days=1)
        return f"{d.strftime('%b %d, %Y')} - {d.strftime('%b %d, %Y')}"

    def expected_this_week_range(self):
        today = date.today()
        start = today - timedelta(days=today.weekday())
        return f"{start:%b %d, %Y} - {today:%b %d, %Y}"

    def expected_last_7_days_range(self):
        today = date.today()
        start = today - timedelta(days=6)
        return f"{start:%b %d, %Y} - {today:%b %d, %Y}"
