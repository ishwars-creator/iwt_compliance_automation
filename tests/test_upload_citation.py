from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from utils.config import USERNAME, PASSWORD


def test_upload_citation(page):
    login = LoginPage(page)
    login.open()  
    login.login(USERNAME, PASSWORD)

    comp = CompliancePage(page)
    comp.goto_compliace_menu()
    comp.goto_mine_details()
    comp.select_company("104")  # 104 value of peabody company
    comp.select_mine("101")  # 101 value of gateway mine
    comp.upload_citataion()

    