class OperatorAnalyticsLocators:
    
    # Tabs
    CITATION_SUMMARY = "role=link[name='Citation Summary']"
    TOP_10 = "role=link[name='Top 10']"
    TRENDS_ANALYSIS = "role=link[name='Trends Analysis']"
    INSPECTION_ANALYSIS = "role=link[name='Inspection Analysis']"

    # Citation Summary Locators
    OPEN_COMPANY_DROPDOWN = "//label[normalize-space()='Company']/following-sibling::select"
    OPEN_MINE_DROPDOWN = "//button[.//span[normalize-space()='Select Mine']]"
    SELECT_ALL_MINES_CHECKBOX = "//label[.//span[normalize-space()='All Mines']]//input[@type='checkbox']"
    OPEN_EVENT_DROPDOWN = "//button[.//span[normalize-space()='Select Event']]"
    SELECT_ALL_EVENTS_CHECKBOX = "//label[.//span[normalize-space()='All Events']]//input[@type='checkbox']"
    DOWNLOAD_SUMMARY_BTN = "//button[normalize-space()='Download Summary']"

    SS_DISTRIBUTION = "role=heading[name='S & S Distribution']"
    SS_BY_MINES = "role=heading[name='S & S by Mine']"
    NEGLIGENCE_DISTRIBUTION = "role=heading[name='Negligence Distribution']"
    NEGLIGENCE_BY_MINE = "role=heading[name='Negligence by Mine']"
    SEVERITY_DISTRIBUTION = "role=heading[name='Severity Distribution']"
    SEVERITY_BY_MINE = "role=heading[name='Severity by Mine']"
    LIKELIHOOD_DISTRIBUTION = "role=heading[name='Likelihood Distribution']"
    LIKELIHOOD_BY_MINE = "role=heading[name='Likelihood by Mine']"
    
    DOWNLOAD_SUMMARY_BTN = "role=button[name='Download Summary']"
    DOWNLOAD_EXCEL_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download Excel']"
    DOWNLOAD_CSV_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download CSV']"
    DOWNLOAD_PDF_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download PDF']"
    DOWNLOAD_EXCEL_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download Excel']"
    DOWNLOAD_CSV_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download CSV']"
    DOWNLOAD_PDF_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download PDF']"
    DOWNLOAD_EXCEL_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download Excel']"
    DOWNLOAD_CSV_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download CSV']"
    DOWNLOAD_PDF_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download PDF']"
    DOWNLOAD_EXCEL_BTN_CHART4 = "//div[@id='chart-container-4']//div[@title='Download Excel']"
    DOWNLOAD_CSV_BTN_CHART4 = "//div[@id='chart-container-4']//div[@title='Download CSV']"
    DOWNLOAD_PDF_BTN_CHART4 = "//div[@id='chart-container-4']//div[@title='Download PDF']"
    
    
    # Top 10 Locators
    TOP_10_EXCEL_BTN_CHART1 = "//div[@id='chart-container-1']//button[@title='Download Excel']"
    TOP_10_CSV_BTN_CHART1 = "//div[@id='chart-container-1']//button[@title='Download CSV']"
    TOP_10_PDF_BTN_CHART1 = "//div[@id='chart-container-1']//button[@title='Download PDF']"
    TOP_10_EXCEL_BTN_CHART2 = "//div[@id='chart-container-2']//button[@title='Download Excel']"
    TOP_10_CSV_BTN_CHART2 = "//div[@id='chart-container-2']//button[@title='Download CSV']"
    TOP_10_PDF_BTN_CHART2 = "//div[@id='chart-container-2']//button[@title='Download PDF']"
    
    TOP_10_BY_TOTAL_PROPESED_PENALTIES = "role=heading[name='Top 10 part section by Total Proposed Penalties']"
    TOP_10_BY_CITATION = "role=heading[name='Top 10 part section by Citations']"
    TOP_25_BY_TOTAL_PROPOSED_PENALTIES = "role=heading[name='Top 25 Violations by Total Proposed Penalties']"
    TOP_25_BY_CITATIONS = "role=heading[name='Top 25 part section by Citations']"
    TOP_40_BY_TOTAL_PROPOSED_PENALTIES = "role=heading[name='Top 40 Violations by Total Proposed Penalties']"
    TOP_40_BY_CITATIONS = "role=heading[name='Top 40 part section by Citations']"
    
    # Trends Analysis Locators
    CITATION_AND_PENALTY = "//h2[normalize-space()='Citations & Penalty']"
    DISTRIBUTION_BY_PART_SECTION = "//h2[normalize-space()='Distribution by Part Section']"
    CITATION_BY_FIELD_OFFICE = "//h2[normalize-space()='Citations by Field Office']"
    
    TRENDS_ANALYSIS_DOWNLOAD_SUMMARY_BTN = "//button[normalize-space()='Download Summary']"
    TRENDS_ANALYSIS_EXCEL_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download Excel']"
    TRENDS_ANALYSIS_CSV_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download CSV']"
    TRENDS_ANALYSIS_PDF_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download PDF']"
    TRENDS_ANALYSIS_EXCEL_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download Excel']"
    TRENDS_ANALYSIS_CSV_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download CSV']"
    TRENDS_ANALYSIS_PDF_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download PDF']"
    TRENDS_ANALYSIS_EXCEL_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download Excel']"
    TRENDS_ANALYSIS_CSV_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download CSV']"
    TRENDS_ANALYSIS_PDF_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download PDF']"
    
    # Inspection Analysis Locators
    INSPECTIONS = "//h2[normalize-space()='Inspections']"
    INSPECTION_TYPE = "//h2[normalize-space()='Inspection Type']"
    VIOLATIONS_BY_INSPECTOR = "//h2[normalize-space()='Violations by Inspector']"
    S_S_VIOLATIONS_BY_INSPECTOR = "//h2[normalize-space()='S&S Violations by Inspector']"
    
    

    INSPECTION_ANALYSIS_DOWNLOAD_SUMMARY_BTN = "//button[normalize-space()='Download Summary']"
    INSPECTION_ANALYSIS_EXCEL_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download Excel']"
    INSPECTION_ANALYSIS_CSV_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download CSV']"
    INSPECTION_ANALYSIS_PDF_BTN_CHART1 = "//div[@id='chart-container-1']//div[@title='Download PDF']"
    INSPECTION_ANALYSIS_EXCEL_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download Excel']"
    INSPECTION_ANALYSIS_CSV_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download CSV']"
    INSPECTION_ANALYSIS_PDF_BTN_CHART2 = "//div[@id='chart-container-2']//div[@title='Download PDF']"
    INSPECTION_ANALYSIS_EXCEL_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download Excel']"
    INSPECTION_ANALYSIS_CSV_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download CSV']"
    INSPECTION_ANALYSIS_PDF_BTN_CHART3 = "//div[@id='chart-container-3']//div[@title='Download PDF']"
    INSPECTION_ANALYSIS_EXCEL_BTN_CHART4 = "//div[@id='chart-container-4']//div[@title='Download Excel']"
    INSPECTION_ANALYSIS_CSV_BTN_CHART4 = "//div[@id='chart-container-4']//div[@title='Download CSV']"
    INSPECTION_ANALYSIS_PDF_BTN_CHART4 = "//div[@id='chart-container-4']//div[@title='Download PDF']"