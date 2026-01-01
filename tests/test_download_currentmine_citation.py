from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.citation_page import CitationPage
from utils.config import USERNAME, PASSWORD
import os

def test_download_company_citation(page):
    login = LoginPage(page)
    login.open()  
    login.login(USERNAME, PASSWORD)

    comp = CompliancePage(page)
    comp.goto_compliace_menu()
    comp.goto_mine_details()
    comp.select_company("115")
    comp.select_mine("111")

    citation = CitationPage(page)
    folder = os.path.join(os.getcwd(), "download/current_mine_citation")

    file_path = citation.download("current mine", folder)

    assert os.path.exists(file_path)
