from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.operator_analytics_trend_analysis_page import OperatorAnalyticsTrendAnalysisPage
from utils.config import USERNAME, PASSWORD
import os

def test_download_trend_analysis_summary(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    op = OperatorAnalyticsTrendAnalysisPage(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.navigate_to_trend_analysis()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()
    op.verify_trend_analysis_loaded()

    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_summary(folder)

    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    

def test_download_trend_analysis_individual_files(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    op = OperatorAnalyticsTrendAnalysisPage(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.navigate_to_trend_analysis()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()

    # download citation and penalty excel
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_citation_penalty_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")
    
    #download citation and penalty csv
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_citation_penalty_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")
    
    #download citation and penalty pdf
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_citation_penalty_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    # download distribution by part section excel
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_distribution_by_part_section_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")

    # download distribution by part section csv
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_distribution_by_part_section_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")

    # download distribution by part section pdf
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_distribution_by_part_section_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    # download citation by field office excel
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_citation_by_field_office_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")
    
    # download citation by field office csv
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_citation_by_field_office_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")
    
    # download citation by field office pdf
    folder = os.path.join(os.getcwd(), "download/op_trend_analysis")
    file_path = op.download_op_trend_analysis_citation_by_field_office_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")