
     
from playwright.sync_api import Page, expect
from locators.operator_analytics_locators import OperatorAnalyticsLocators as opl
import os
from datetime import datetime




class OperatorAnalyticsTrendAnalysisPage:
    
    
    def __init__(self, page: Page):
        self.page = page
    
    
    def goto_compliace_menu(self):
        self.page.get_by_role("link", name="Compliance").click()
        expect(self.page.get_by_text("Compliance").nth(1)).to_be_visible()    


    def navigate_to_top10(self):
        self.page.locator(opl.TOP_10).click()
        
    def navigate_to_trend_analysis(self):
        self.page.locator(opl.TRENDS_ANALYSIS).click()    

    def select_company(self):
        self.page.locator(opl.OPEN_COMPANY_DROPDOWN).select_option(value="122")
        

    def select_all_mines(self):
        self.page.locator(opl.OPEN_MINE_DROPDOWN).click()
        self.page.locator(opl.SELECT_ALL_MINES_CHECKBOX).check()
        
    def select_all_events(self):
        self.page.locator(opl.OPEN_EVENT_DROPDOWN).click()
        self.page.locator(opl.SELECT_ALL_EVENTS_CHECKBOX).check()   
        
         
    def verify_trend_analysis_loaded(self):
        expect(self.page.locator(opl.CITATION_AND_PENALTY)).to_be_visible()
        expect(self.page.locator(opl.DISTRIBUTION_BY_PART_SECTION)).to_be_visible()
        expect(self.page.locator(opl.CITATION_BY_FIELD_OFFICE)).to_be_visible()

        
    def download_op_trend_analysis_summary(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.DOWNLOAD_SUMMARY_BTN).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path

    def download_op_trend_analysis_citation_penalty_excel(self,folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_EXCEL_BTN_CHART1).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path

    def download_op_trend_analysis_citation_penalty_csv(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_CSV_BTN_CHART1).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_trend_analysis_citation_penalty_pdf(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_PDF_BTN_CHART1).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path


    def download_op_trend_analysis_distribution_by_part_section_excel(self,folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_EXCEL_BTN_CHART2).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path

    def download_op_trend_analysis_distribution_by_part_section_csv(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_CSV_BTN_CHART2).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path

    def download_op_trend_analysis_distribution_by_part_section_pdf(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_PDF_BTN_CHART2).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    
    def download_op_trend_analysis_citation_by_field_office_excel(self,folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_EXCEL_BTN_CHART3).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_trend_analysis_citation_by_field_office_csv(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_CSV_BTN_CHART3).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path
    
    def download_op_trend_analysis_citation_by_field_office_pdf(self, folder):
        with self.page.expect_download(timeout=60000) as download_info:
            self.page.locator(opl.TRENDS_ANALYSIS_PDF_BTN_CHART3).click()

        download = download_info.value
        os.makedirs(folder, exist_ok=True)
        name, ext = os.path.splitext(download.suggested_filename)
        timestamp = datetime.now().strftime("%Y-%m-%d_%I.%M.%S_%p")
        file_path = os.path.join(folder, f"{name}_{timestamp}{ext}")
        download.save_as(file_path)
        return file_path