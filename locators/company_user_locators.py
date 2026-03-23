class CompanyUserLocators:
    
    SETTINGS_MENU = "a[href='/app/Setting/users']"

    HEADING = "Company Users"
    ADD_USER_BTN = "//button[@id='add_new_user']"
    FIRSTNAME = "//input[@id='firstName']"
    LASTNAME = "//input[@id='lastName']"
    EMAIL = "//input[@name='email']"
    CONFIRM_EMAIL = "//input[@id='cEmail']"

    ADD_BTN = "//button[@id='create_user']"
    SUBMIT_BTN = "//button[@type='submit']"
    SEARCH_BOX = "input[placeholder='Search User']"