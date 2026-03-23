import re
from playwright.sync_api import Page, expect
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.company_page import CompanyPage
from utils.config import USERNAME, PASSWORD
from utils.testdata import COMPANY


def test_example(page: Page) -> None:
    page.goto("https://qaportal.iwtanalytics.com/app")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("IwtUser")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("X4ZP~#ic")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("row", name=(COMPANY['name'])).locator("#deleteCompany").click()
    page.get_by_role("button", name="Cancel").click()
