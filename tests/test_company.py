from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.company_page import CompanyPage
from utils.testdata import COMPANY
from utils.config import USERNAME, PASSWORD

def test_add_company(page):
    # LoginPage(page).login(USERNAME, PASSWORD)
    
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    company = CompanyPage(page)
    company.verify_company_page_loaded()
    
    # Get existing company list, If company exists,delete first & then add same company

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