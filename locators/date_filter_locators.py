class DateFilterLocators:

    # Date range input (stable)
    DATE_RANGE_INPUT = "//input[@type='text' and contains(@class,'tracking-wide')]"

    # Date picker popup container (dark/light safe)
    DATE_PICKER_POPUP = "//div[contains(@class,'custom-datepicker')]"

    # Predefined date option
    PREDEFINED_OPTION = (
        "//ul[contains(@class,'tracking-wide')]"
        "//li[normalize-space()='{option}']"
    )
