class CompanyLocators:
    HEADING = "Company Management"
    ADD_COMPANY_BTN = "Add Company"
    SAP_ID = "input[name='sapAccountId']"
    MSHA_NAME = "input[name='mshaName']"
    ADDRESS = "input[name='addressLine1']"
    STATE = "select[name='stateId']"
    CITY = "select[name='cityId']"
    ZIP = "input[name='zipcode']"
    PHONE = "input[name='phone']"
    ADD_CORP_ADMIN_BTN = "//button[@type='button'][.//span[text()='Add']]"
    FIRSTNAME = "//input[@id='firstName']"
    LASTNAME = "//input[@id='lastName']"
    EMAIL = "//input[@id='emailId']"
    CONFIRM_EMAIL = "//input[@id='confirmEmail']"
    
    SUBMIT_BTN = "//button[@type='submit']"
    SEARCH_BOX = "input[placeholder='Search Company']"
    
    # New Module Access Locators
    MODULE_LOCATION = "span:text('Location')"
    MODULE_PRODUCTION = "span:text('Production')"
    MODULE_ATMOSPHERE = "span:text('Atmosphere')"
    MODULE_COMPLIANCE = "span:text('Compliance')"
    MODULE_FORMS = "span:text('Forms')"
    
    ## Action buttons
    COMPANY_TOGGLE_BTN = "//tr[td[normalize-space()='Lhoist Group']]//input[@type='checkbox']"
    EDIT_COMPANY_BTN = "//tr[td[normalize-space()='Lhoist Group']]//button[@id='editCompany']"
    DELETE_COMPANY_BTN = "//tr[td[normalize-space()='Lhoist Group']]//button[@id='deleteCompany']"
    ADD_COMPANY_USER_BTN = "//tr[td[normalize-space()='Lhoist Group']]//button[@id='addCompanyUser']"
    ADD_MINE_BTN = "//tr[td[normalize-space()='Lhoist Group']]//button[@id='addCompanyMine']"
    
    
    
    

    
    
    