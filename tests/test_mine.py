from pages.login_page import LoginPage
from pages.mine_page import MinePage
from utils.testdata import MINE
from utils.config import USERNAME, PASSWORD

def test_add_mine(page):
    LoginPage(page).login(USERNAME, PASSWORD)
    mine = MinePage(page)
    mine.open_company("Steve McGee")
    mine.add_mine(MINE)
