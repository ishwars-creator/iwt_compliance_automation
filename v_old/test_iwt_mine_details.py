import os
import re
from playwright.sync_api import Page, expect
from config import USERNAME, PASSWORD, URL


def test_render_citataion_table(page: Page) -> None:
    # Navigate to the portal
    page.goto(URL)

    # Login
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()

    # Navigate to Compliance module
    page.get_by_role("link", name="Compliance").click()
    expect(page.get_by_text("Compliance").nth(1)).to_be_visible()

    # Select company (assuming the first combobox is company selection)
    company_dropdown = page.get_by_role("combobox").first
    company_dropdown.select_option("136")

    # Select mine
    mine_dropdown = page.locator(
        "div", has_text=re.compile(r"^MineSelect Mine3 M Corona Plant$")
    ).get_by_role("combobox")
    mine_dropdown.select_option("110")

    # Verify Compliance page elements
    expect(page.get_by_role("heading", name="Mine Details - Citations")).to_be_visible()
    expect(page.get_by_role("button", name="Upload Citations")).to_be_visible()
    expect(page.get_by_text("Actions")).to_be_visible()
    expect(page.get_by_role("button", name="csv-download")).to_be_visible()

    # Logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
    
    


def test_search_citation_order_number(page: Page) -> None:
    # Navigate to the portal
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    # Login
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()

    # Navigate to Compliance module
    page.get_by_role("link", name="Compliance").click()
    expect(page.get_by_text("Compliance").nth(1)).to_be_visible()

    # Select Company
    company_dropdown = page.get_by_role("combobox").first
    company_dropdown.select_option("136")

    # Select Mine
    mine_dropdown = page.locator(
        "div", has_text=re.compile(r"^MineSelect Mine3 M Corona Plant$")
    ).get_by_role("combobox")
    mine_dropdown.select_option("110")

    # Search Citation Order Number
    citation_order_no = "9892830"
    search_box = page.get_by_role("textbox", name="Search")
    search_box.click()
    search_box.fill(citation_order_no)

    # Verify search result
    page.wait_for_selector(f"text={citation_order_no}", timeout=10000)
    expect(page.get_by_text(citation_order_no)).to_be_visible()
    
    # Logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()