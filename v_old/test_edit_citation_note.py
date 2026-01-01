import os
import re
from playwright.sync_api import Page, expect
from config import USERNAME, PASSWORD, URL


def test_upload_citation_image(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    

    # Wait for main dashboard
    expect(page.get_by_role("link", name="Compliance")).to_be_visible(timeout=20000)
    page.get_by_role("link", name="Compliance").click()

    # Select company & mine
    page.get_by_role("combobox").nth(0).select_option("136")  # Company: Peabody Energy
    page.locator("div", has_text=re.compile(r"^MineSelect Mine3 M Corona Plant$")).get_by_role("combobox").select_option("110")

    # Open citation note
    page.get_by_role("row", name=re.compile(r"9890537")).locator("path").first.click()
    expect(page.get_by_text("Citation Note: 9890537")).to_be_visible(timeout=10000)
    
    page.locator("div").filter(has_text=re.compile(r"^Citation Note: 9890537$")).get_by_role("button").click()
    
    # --- Define file path ---
    current_wrk_directory = os.getcwd()
    uplod_img = os.path.join(current_wrk_directory, "test_data", "pexels-optical.jpg")
    uplod_pdf = os.path.join(current_wrk_directory, "test_data", "9783475.pdf")
    assert os.path.exists(uplod_img), f"File not found: {uplod_img}"
    
    # upload image
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Upload Image").click()
    file_chooser = fc_info.value
    file_chooser.set_files(uplod_img)
    
    # upload pdf
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Upload PDF").click()
    file_chooser = fc_info.value
    file_chooser.set_files(uplod_pdf)

    # Click Save
    page.get_by_role("button", name="Save").click()

    # Assert success message
    expect(page.get_by_text("Citation notes updated")).to_be_visible(timeout=10000)
