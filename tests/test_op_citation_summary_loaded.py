from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.operator_analytics_citation_sum_page import OperatorAnalyticsPage
from utils.config import USERNAME, PASSWORD

def test_operator_analytics_citation_summary_loaded(page):
    login = LoginPage(page)
    login.open()  
    login.login(USERNAME, PASSWORD)

    op = OperatorAnalyticsPage(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()
    op.verify_citation_summarys_loaded()
