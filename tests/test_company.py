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
    company.open_add_company_form()
    company.add_company(COMPANY)
