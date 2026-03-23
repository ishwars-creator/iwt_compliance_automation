import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD, URL
from utils.testdata import COMPANY, MINE, COMPANY_USERS
from pages.company_page import CompanyPage
from pages.mine_page import MinePage
from pages.company_user_page import CompanyUserPage
from pages.dashboard_page import dashboardpage
from pages.compliance_page import CompliancePage
from pages.citation_page import CitationPage
import os




# Create one browser context for entire test session
@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    # Login only once
    page.goto(URL)
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    yield page

    # Close only after ALL tests finished
    context.close()

# =========================
#         TESTS
# =========================

def test_add_company(page):
    company = CompanyPage(page)
    company.verify_company_page_loaded()
    
    # Get existing company list, If company exists,delete first & then add same mine

    company_name_locator = page.locator("//tbody//tr/td[2]//div[contains(@class,'cursor-pointer')]")
    company_names = [name.strip() for name in company_name_locator.all_inner_texts()]
    print("Existing companies:", company_names)
    
    if COMPANY["name"] in company_names:
        print(f"Company '{COMPANY['name']}' exists. Deleting first...")        
        page.get_by_role("row", name=(COMPANY['name'])).locator("#deleteCompany").click()
        page.get_by_role("button", name="Delete", exact=True).click()
        expect(page.get_by_text("Company deleted successfully")).to_be_visible(timeout=15000)
        
    # Add company   
    company.open_add_company_form()
    company.add_company(COMPANY)

def test_add_mine(page):
    mine = MinePage(page)
    mine.open_company("Lhoist Group")
    mine.add_mine(MINE)

    
    
def test_add_corp_admin(page):
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_corp_admin(COMPANY_USERS)
    


def test_add_corp_manager(page):
    cp = CompanyUserPage(page)
    cp.add_corp_manager(COMPANY_USERS)


def test_add_mine_admin(page):
    cp = CompanyUserPage(page)
    cp.add_mine_admin(COMPANY_USERS)

def test_add_mine_manager(page):
    cp = CompanyUserPage(page)   
    cp.add_mine_manager(COMPANY_USERS)

def test_add_mine_user(page):
    cp = CompanyUserPage(page) 
    cp.add_mine_user(COMPANY_USERS)

  
    
def test_compliance_dashboard(page):
    dash = dashboardpage(page)
    dash.goto_compliace_menu()
    dash.select_company("115")
    dash.select_all_mines()
    dash.verify_dashboard_loaded()



def test_download_company_citation(page):

    comp = CompliancePage(page)
    comp.goto_compliace_menu()
    comp.goto_mine_details()
    comp.select_company("115")
    comp.select_mine("111")

    citation = CitationPage(page)
    folder = os.path.join(os.getcwd(), "download/company_citation")
    file_path = citation.download("company", folder)
    assert os.path.exists(file_path)
    cp = CompanyPage(page)
    cp.navigate_to_company_list() 
    
def test_download_current_mine_citation(page):

    comp = CompliancePage(page)
    comp.goto_compliace_menu()
    comp.goto_mine_details()
    comp.select_company("115")
    comp.select_mine("111")

    citation = CitationPage(page)
    folder = os.path.join(os.getcwd(), "download/current_mine_citation")
    file_path = citation.download("current mine", folder)
    assert os.path.exists(file_path)    