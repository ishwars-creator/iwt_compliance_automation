from pages.date_filter_page import DateFilterPage


class TestPredefinedDateFilters:

    def test_today_filter(self, compliance_page):
        date_page = DateFilterPage(compliance_page)

        date_page.open_date_picker()
        date_page.select_predefined_option("Today")

        assert date_page.get_selected_date_range() == date_page.expected_today_range()

    def test_yesterday_filter(self, compliance_page):
        date_page = DateFilterPage(compliance_page)

        date_page.open_date_picker()
        date_page.select_predefined_option("Yesterday")

        assert date_page.get_selected_date_range() == date_page.expected_yesterday_range()

    def test_this_week_filter(self, compliance_page):
        date_page = DateFilterPage(compliance_page)

        date_page.open_date_picker()
        date_page.select_predefined_option("This Week")

        assert date_page.get_selected_date_range() == date_page.expected_this_week_range()

    def test_last_7_days_filter(self, compliance_page):
        date_page = DateFilterPage(compliance_page)

        date_page.open_date_picker()
        date_page.select_predefined_option("Last 7 days")

        assert date_page.get_selected_date_range() == date_page.expected_last_7_days_range()
