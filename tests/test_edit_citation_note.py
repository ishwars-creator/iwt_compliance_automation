from pages.login_page import LoginPage
from pages.compliance_page import CompliancePage
from pages.citation_page import CitationPage
from utils.config import USERNAME, PASSWORD
import os

def test_edit_citation_note(page):
    login = LoginPage(page)
    login.open()  
    login.login(USERNAME, PASSWORD)

    comp = CompliancePage(page)
    comp.goto_compliace_menu()
    comp.goto_mine_details()
    comp.select_company("115")
    comp.select_mine("111")
    comp.open_citation_notes("5104192")
    comp.fill_data_in_citation_note()
    comp.click_save_citation_note_btn()    