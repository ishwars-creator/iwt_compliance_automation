from pages.login_page import LoginPage
from pages.mine_page import MinePage
from utils.testdata import MINE
from utils.config import USERNAME, PASSWORD

def test_add_mine(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    mine = MinePage(page)
    mine.open_company("Lhoist Group")
    mine.add_mine(MINE)
    
def test_edit_mine(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    mine = MinePage(page)
    mine.open_company("Lhoist Group")
    mine.edit_mine("updated adress line 2")  
    
