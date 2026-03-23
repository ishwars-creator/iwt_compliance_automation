
     
from playwright.sync_api import Page, expect
from locators.operator_analytics_locators import OperatorAnalyticsLocators as opl
import os
from datetime import datetime




class OperatorAnalyticsPage:
    
    
    def __init__(self, page: Page):
        self.page = page
    
    
    def goto_compliace_menu(self):
        self.page.get_by_role("link", name="Compliance").click()
        expect(self.page.get_by_text("Compliance").nth(1)).to_be_visible()    
    
        
    def select_company(self):
        self.page.locator(opl.OPEN_COMPANY_DROPDOWN).select_option(value="122")
        

    def select_all_mines(self):
        self.page.locator(opl.OPEN_MINE_DROPDOWN).click()
        self.page.locator(opl.SELECT_ALL_MINES_CHECKBOX).check()
        
    def select_all_events(self):
        self.page.locator(opl.OPEN_EVENT_DROPDOWN).click()
        self.page.locator(opl.SELECT_ALL_EVENTS_CHECKBOX).check()   
        
         
    def verify_citation_summarys_loaded(self):
        expect(self.page.locator(opl.SS_DISTRIBUTION)).to_be_visible()
        expect(self.page.locator(opl.SS_BY_MINES)).to_be_visible()
        expect(self.page.locator(opl.NEGLIGENCE_DISTRIBUTION)).to_be_visible()
        expect(self.page.locator(opl.NEGLIGENCE_BY_MINE)).to_be_visible()
        expect(self.page.locator(opl.SEVERITY_DISTRIBUTION)).to_be_visible()
        expect(self.page.locator(opl.SEVERITY_BY_MINE)).to_be_visible()
        expect(self.page.locator(opl.LIKELIHOOD_DISTRIBUTION)).to_be_visible()
        expect(self.page.locator(opl.LIKELIHOOD_BY_MINE)).to_be_visible()
        
        
        
    def download_op_citation_summary(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_SUMMARY_BTN).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path

    def download_op_sands_distribution_excel(self,folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_EXCEL_BTN_CHART1).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_sands_distribution_csv(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_CSV_BTN_CHART1).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_sands_distribution_pdf(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_PDF_BTN_CHART1).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    
    def download_op_negligence_distribution_excel(self,folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_EXCEL_BTN_CHART2).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_negligence_distribution_csv(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_CSV_BTN_CHART2).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_negligence_distribution_pdf(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_PDF_BTN_CHART2).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_severity_distribution_excel(self,folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_EXCEL_BTN_CHART3).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_severity_distribution_csv(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_CSV_BTN_CHART3).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_severity_distribution_pdf(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_PDF_BTN_CHART3).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_likelihood_distribution_excel(self,folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_EXCEL_BTN_CHART4).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_likelihood_distribution_csv(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_CSV_BTN_CHART4).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_likelihood_distribution_pdf(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_PDF_BTN_CHART4).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    