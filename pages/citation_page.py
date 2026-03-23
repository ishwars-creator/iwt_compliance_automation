import os
from core.base_page import BasePage
from playwright.sync_api import expect
import re
from datetime import datetime

class CitationPage(BasePage):

    def download(self, option, folder):
        with self.page.expect_download() as download_info:
            self.page.get_by_role("button", name=re.compile("CSV|Download", re.I)).click()
            self.page.get_by_role("button", name=option).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path

    def upload(self, file_path):
        self.page.get_by_role("button", name="Upload Citations").click()

        with self.page.expect_file_chooser() as fc:
            self.page.get_by_text("Click to Upload file").click()

        fc.value.set_files(file_path)

        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Citation uploaded successfully")).to_be_visible()

    def open_column_panel(self):
        self.page.locator("text=Columns(").click()
