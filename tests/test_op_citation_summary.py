from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.operator_analytics_page import operatoranalyticspage
from utils.config import USERNAME, PASSWORD


def test_dashboard(page):
    login = LoginPage(page)
    login.open()  
    login.login(USERNAME, PASSWORD)

    op = operatoranalyticspage(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.select_company("115")
    op.select_all_mines()
    op.select_all_events()
    op.verify_citation_summary()