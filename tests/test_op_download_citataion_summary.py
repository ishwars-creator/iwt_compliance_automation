from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.operator_analytics_citation_sum_page import OperatorAnalyticsPage
from utils.config import USERNAME, PASSWORD
import os


def test_download_op_citation_summary(page):
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

    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_citation_summary(folder)

    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")


def test_download_op_citation_summary_individual_chart(page):
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

    #download s&s excel
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_sands_distribution_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")
    
    #download s&s csv
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_sands_distribution_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")
    
    #download s&s pdf
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_sands_distribution_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    # download niegligence excel
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_negligence_distribution_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")

    # download niegligence csv
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_negligence_distribution_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")

    # download niegligence pdf
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_negligence_distribution_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    # download severity excel
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_severity_distribution_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")

    # download severity csv
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_severity_distribution_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")

    # download severity pdf
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_severity_distribution_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")
    
    # download likelihood excel
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_likelihood_distribution_excel(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".xlsx")

    # download likelihood csv
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_likelihood_distribution_csv(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".csv")

    # download likelihood pdf
    folder = os.path.join(os.getcwd(), "download/op_citation_summary")
    file_path = op.download_op_likelihood_distribution_pdf(folder)
    assert os.path.exists(file_path)
    assert file_path.endswith(".pdf")