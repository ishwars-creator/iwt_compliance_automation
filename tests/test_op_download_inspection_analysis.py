from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.operator_analytics_inspection_analysis_page import OperatorAnalyticsInspectionAnalysisPage
from utils.config import USERNAME, PASSWORD
import os

def test_download_inspection_analysis_summary(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    op = OperatorAnalyticsInspectionAnalysisPage(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.navigate_to_inspection_analysis()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()
    op.verify_inspection_analysis_loaded()
    
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_summary(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    

def test_download_inspection_analysis_individual_files(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    op = OperatorAnalyticsInspectionAnalysisPage(page)
    op.goto_compliace_menu()
    CompliancePage(page).goto_operator_analytics()
    op.navigate_to_inspection_analysis()
    op.select_company()
    op.select_all_mines()
    op.select_all_events()

    # download inspection excel
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_inspection_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")
    
    #download inspection csv
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_inspection_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")
    
    #download inspection pdf
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_inspection_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")

    # # download inspection type excel
    # folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    # file_path = op.download_op_inspection_analysis_inspection_type_excel(folder)
    # assert os.path.exists(file_path)
    # assert file_path.endswith(".xlsx")

    # # download inspection type csv
    # folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    # file_path = op.download_op_inspection_analysis_inspection_type_csv(folder)
    # assert os.path.exists(file_path)
    # assert file_path.endswith(".csv")

    # # download inspection type pdf
    # folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    # file_path = op.download_op_inspection_analysis_inspection_type_pdf(folder)
    # assert os.path.exists(file_path)
    # assert file_path.endswith(".pdf")
    
    # download violation excel
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_violation_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")
    
    # download violation csv
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_violation_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")
    
    # download violation pdf
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_violation_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    # download ss violation excel
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_ss_violation_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")
    
    # download ss violation csv
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_ss_violation_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")
    
    # download ss violation pdf
    folder = os.path.join(os.getcwd(), "download/op_inspection_analysis")
    file_path = op.download_op_inspection_analysis_ss_violation_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")