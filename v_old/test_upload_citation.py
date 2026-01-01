import os
import re
from playwright.sync_api import Page, expect
from config import USERNAME, PASSWORD, URL


def test_upload_citation(page: Page) -> None:
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    # --- Login ---
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()

    # --- Navigate to Compliance ---
    page.get_by_role("link", name="Compliance").click()
    expect(page.get_by_text("Compliance").nth(1)).to_be_visible(timeout=20000)

    # --- Select Company and Mine ---
    page.get_by_role("combobox").first.select_option("137")
    page.locator(
        "div", has_text=re.compile(r"^MineSelect MineGateway Mine North$")
    ).get_by_role("combobox").select_option("111")

    # --- Open Upload Citation modal ---
    page.get_by_role("button", name="Upload Citations").click()
    expect(page.get_by_text("Upload Citation for Gateway Mine North")).to_be_visible(timeout=10000)
    page.wait_for_timeout(2000)  # small delay for modal animation

    # --- Define file path ---
    current_wrk_directory = os.getcwd()
    uplod_pdf = os.path.join(current_wrk_directory, "test_data", "9783475.pdf")
    
    # upload citataion
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Click to Upload file").click()
    file_chooser = fc_info.value
    file_chooser.set_files(uplod_pdf)
    
    # --- Click Save ---
    page.get_by_role("button", name="Save").click()

    # --- Validate upload success ---
    expect(page.get_by_text("Scan complete")).to_be_visible(timeout=30000)
    expect(page.get_by_text("Citation uploaded successfully")).to_be_visible(timeout=30000)

    # --- Logout ---
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
