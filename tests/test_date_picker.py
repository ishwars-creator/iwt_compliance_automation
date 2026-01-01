from playwright.sync_api import Page, expect
from datetime import datetime, timedelta

from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from utils.config import USERNAME, PASSWORD
from calendar import monthrange



def format_date(date_obj):
    return date_obj.strftime("%b %d, %Y")

def subtract_months(date_obj, months):
    year = date_obj.year
    month = date_obj.month - months

    while month <= 0:
        month += 12
        year -= 1

    day = min(date_obj.day, monthrange(year, month)[1])
    return date_obj.replace(year=year, month=month, day=day)



def test_mine_details_date_filter(page: Page) -> None:
    login = LoginPage(page)
    login.open()  
    login.login(USERNAME, PASSWORD)

    comp = CompliancePage(page)
    comp.goto_compliace_menu()
    comp.goto_mine_details()
    comp.select_company("115")
    comp.select_mine("111")

    # ---------- Date Input ----------
    date_input = page.locator("input[placeholder='MMM DD, YYYY - MMM DD, YYYY']")

    today = datetime.today()
    yesterday = today - timedelta(days=1)
    
    start_of_this_week = today - timedelta(days=today.weekday())
    end_of_this_week = start_of_this_week + timedelta(days=6)

    start_of_last_week = start_of_this_week - timedelta(days=7)
    end_of_last_week = start_of_this_week - timedelta(days=1)
    

    # ---------- Month Calculations ----------
    start_of_this_month = today.replace(day=1)
    end_of_this_month = today.replace(
        day=monthrange(today.year, today.month)[1]
    )

    # Last Month
    last_month_end = start_of_this_month - timedelta(days=1)
    start_of_last_month = last_month_end.replace(day=1)

    # ---------- Multi-Month Calculations ----------
    last_6_month_start = subtract_months(today, 6)
    last_12_month_start = subtract_months(today, 12)


    # ---------- Year Calculations ----------
    start_of_year = today.replace(month=1, day=1)


    # ---------- Today ----------
    date_input.click()
    page.get_by_text("Today").click()

    expected_today = f"{format_date(today)} - {format_date(today)}"
    expect(date_input).to_have_value(expected_today)

    # ---------- Yesterday ----------
    date_input.click()
    page.get_by_text("Yesterday").click()

    expected_yesterday = f"{format_date(yesterday)} - {format_date(yesterday)}"
    expect(date_input).to_have_value(expected_yesterday)

    # ---------- This Week ----------
    date_input.click()
    page.get_by_text("This Week").click()

    expected_this_week = (
        f"{format_date(start_of_this_week)} - {format_date(end_of_this_week)}"
    )
    expect(date_input).to_have_value(expected_this_week)
    
    # ---------- Last Week ----------
    date_input.click()
    page.get_by_text("Last Week").click()

    expected_last_week = (
    f"{format_date(start_of_last_week)} - {format_date(end_of_last_week)}"
    )
    expect(date_input).to_have_value(expected_last_week)
    
    # ---------- This month ----------
    date_input.click()
    page.get_by_text("This Month").click()

    expected_this_month = (
    f"{format_date(start_of_this_month)} - {format_date(end_of_this_month)}"
    )
    expect(date_input).to_have_value(expected_this_month)
    
    # ---------- Last month ----------
    date_input.click()
    page.get_by_text("Last Month").click()

    expected_last_month = (
    f"{format_date(start_of_last_month)} - {format_date(last_month_end)}"
    )
    expect(date_input).to_have_value(expected_last_month)
    
    # ---------- Last 6 months ----------
    
    date_input.click()
    page.get_by_text("Last 6 Months").click()

    expected_last_6_months = (
    f"{format_date(last_6_month_start)} - {format_date(today)}"
    )
    expect(date_input).to_have_value(expected_last_6_months)
    
    # ---------- Last 12 months ----------
    date_input.click()
    page.get_by_text("Last 12 Months").click()

    expected_last_12_months = (
    f"{format_date(last_12_month_start)} - {format_date(today)}"
    )
    expect(date_input).to_have_value(expected_last_12_months)
    
    # ---------- Year to Date ----------
    date_input.click()
    page.get_by_text("Year to Date").click()

    expected_ytd = (
    f"{format_date(start_of_year)} - {format_date(today)}"
    )
    expect(date_input).to_have_value(expected_ytd)