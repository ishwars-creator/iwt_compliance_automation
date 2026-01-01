from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.dashboard_page import dashboardpage
from utils.config import USERNAME, PASSWORD


def test_dashboard(page):
    login = LoginPage(page)
    login.open()  
    login.login(USERNAME, PASSWORD)

    dash = dashboardpage(page)
    dash.goto_compliace_menu()
    dash.select_company("115")
    dash.select_all_mines()
    dash.verify_dashboard_loaded()