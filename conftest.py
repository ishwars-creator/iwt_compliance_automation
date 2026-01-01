import pytest
from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from utils.config import USERNAME, PASSWORD

@pytest.fixture
def compliance_page(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    comp = CompliancePage(page)
    comp.goto_compliace_menu()
    comp.goto_mine_details()
    comp.select_company("115")
    comp.select_mine("111")

    return page
