class ComplianceLocators:
    COMPANY_DROPDOWN = "//select//option[@title='Barrick Nevada Holding LLC; Newmont USA Limited']"
    DASHBOARD = "//a[normalize-space()='Dashboard']"
    MINE_DETAILS = "//a[normalize-space()='Mine Details']"
    MINE_SUMMARY = "//a[normalize-space()='Mine Summary']"
    MINE_ANALYTICS ="//a[normalize-space()='Mine Analytics']"
    OPERATOR_ANALYTICS = "//a[normalize-space()='Operator Analytics']"
    CHATBOT = "//a[normalize-space()='Chatbot']"
    
    # mine details page locator
    UPLOAD_CITATIONS_BTN = "#upload_citations"
    SAVE_CITATION_BTN = "//button[normalize-space()='Save']" 
    CITATION_NOTE_ICON = "svg:has(title:has-text('Citation Notes'))"
    #Edit citation note
    EDIT_CITATION_NOTE_ICON = "//button[contains(@class,'edit-icon')]"
    NOTES_TEXTAREA = "//label[normalize-space()='Notes']/following-sibling::textarea"
    ROOT_CAUSE_TEXTAREA = "//label[normalize-space()='Notes']/parent::div/following-sibling::div//textarea"
    SAVE_CITATION_NOTE_BTN = "//button[normalize-space()='Save']"

    #search citation
    SEARCH_CITATION_INPUT = "//input[@id='search-result']"
    
    
    
    
