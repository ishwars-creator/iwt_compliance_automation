from core.base_page import BasePage
from locators.compliance_locators import ComplianceLocators as C
from playwright.sync_api import expect
import os

class CompliancePage(BasePage):

    def goto_compliace_menu(self):
        self.page.get_by_role("link", name="Compliance").click()
        expect(self.page.get_by_text("Compliance").nth(1)).to_be_visible()
        
    def goto_mine_details(self):
        self.page.locator(C.MINE_DETAILS).click()        

    def select_company(self, value):
        self.page.get_by_role("combobox").nth(0).select_option(value)

    def select_mine(self, value):
        self.page.get_by_role("combobox").nth(1).select_option(value)
        self.wait_for_table_load()
        
        
    def upload_citataion(self):
        self.page.locator(C.UPLOAD_CITATIONS_BTN).click()
        expect(self.page.get_by_text("Upload Citation for Gateway Mine North")).to_be_visible()
        # --- Define file path ---
        current_wrk_directory = os.getcwd()
        uplod_pdf = os.path.join(current_wrk_directory, "test_data", "9783475.pdf")
    
        # upload citataion
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Click to Upload file").click()
        file_chooser = fc_info.value
        file_chooser.set_files(uplod_pdf)    
        
         # --- Click Save ---
        self.page.locator(C.SAVE_CITATION_BTN).click()

        # --- Validate upload success ---
        expect(self.page.get_by_text("Scan complete")).to_be_visible(timeout=30000)
        self.page.locator(C.SAVE_CITATION_BTN).click()
        expect(self.page.get_by_text("Citation uploaded successfully")).to_be_visible(timeout=30000)
                

    def open_citation_notes(self, citation_no):
        self.page.locator("tr", has_text=citation_no).locator(C.CITATION_NOTE_ICON).click()
        
        
    def fill_data_in_citation_note(self):
        self.page.locator(C.EDIT_CITATION_NOTE_ICON).click()
        # self.page.locator(C.NOTES_TEXTAREA).click()
        self.page.locator(C.NOTES_TEXTAREA).fill("TEST Root cause")
        # self.page.locator(C.ROOT_CAUSE_TEXTAREA).click()
        self.page.locator(C.ROOT_CAUSE_TEXTAREA).fill("TEST notes")
        
        
        # --- Define file path ---
        current_wrk_directory = os.getcwd()
        uplod_img = os.path.join(current_wrk_directory, "test_data", "pexels-optical.jpg")
        uplod_pdf = os.path.join(current_wrk_directory, "test_data", "9783475.pdf")
        assert os.path.exists(uplod_img), f"File not found: {uplod_img}"
        
        # upload image
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Upload Image").click()
        file_chooser = fc_info.value
        file_chooser.set_files(uplod_img)
        
        # upload pdf
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Upload PDF").click()
        file_chooser = fc_info.value
        file_chooser.set_files(uplod_pdf)
        
    def click_save_citation_note_btn(self):    
        self.page.locator(C.SAVE_CITATION_BTN).click()
        expect(self.page.get_by_text("Citation notes updated")).to_be_visible(timeout=30000)
        
    
    def search_citation(self, citation_no):
        self.page.locator(C.SEARCH_CITATION_INPUT).click()
        self.page.locator(C.SEARCH_CITATION_INPUT).fill(citation_no)
        self.wait_for_table_load()
        expect(self.page.locator("tr", has_text=citation_no)).to_be_visible(timeout=30000)
                
        
        
        
    
        
