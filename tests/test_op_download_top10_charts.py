from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.operator_analytics_top10_page import OperatorAnalyticsTop10Page
from utils.config import USERNAME, PASSWORD
import os

def test_download_top10_summary(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    op = OperatorAnalyticsTop10Page(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.navigate_to_top10()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()
    op.verify_top10_charts_loaded()

    folder = os.path.join(os.getcwd(), "download/op_top10_charts")
    file_path = op.download_op_top10_summary(folder)

    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    

def test_download_top10_indiviual_files(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    op = OperatorAnalyticsTop10Page(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.navigate_to_top10()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()

    # download top10 part section by total propesed penalties excel
    folder = os.path.join(os.getcwd(), "download/op_top10_charts")
    file_path = op.download_op_top10_total_proposed_penalty_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")
    
    #download top10 part section by total propesed penalties csv
    folder = os.path.join(os.getcwd(), "download/op_top10_charts")
    file_path = op.download_op_top10_total_proposed_penalty_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")
    
    #download top10 part section by total propesed penalties pdf
    folder = os.path.join(os.getcwd(), "download/op_top10_charts")
    file_path = op.download_op_top10_total_proposed_penalty_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    # download top10 part section by citations excel
    folder = os.path.join(os.getcwd(), "download/op_top10_charts")
    file_path = op.download_op_top10_part_section_by_citation_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")

    # download top10 part section by citations csv
    folder = os.path.join(os.getcwd(), "download/op_top10_charts")
    file_path = op.download_op_top10_part_section_by_citation_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")

    # download top10 part section by citations pdf
    folder = os.path.join(os.getcwd(), "download/op_top10_charts")
    file_path = op.download_op_top10_part_section_by_citation_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
