from playwright.sync_api import Page, expect
from config import USERNAME, PASSWORD, URL

def test_select_citation_column(page: Page) -> None:
  
   # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
     # --- Navigate to Compliance ---
    page.get_by_role("link", name="Compliance").click()
    expect(page.get_by_text("Compliance").nth(1)).to_be_visible(timeout=20000)

    
    # --- Select Company ---
    company_dropdown = page.get_by_role("combobox").nth(0)
    company_dropdown.select_option("104")       # Single selection is enough

    # --- Select Mine ---
    mine_dropdown = page.get_by_role("combobox").nth(1)
    mine_dropdown.select_option("101")
    
    page.wait_for_selector("text=Mine Details - Citations")
 
    # Open “Columns” panel
    page.locator("text=Columns(").click()
    page.wait_for_selector("text=List of Columns Names")
    
    page.get_by_text("Action To Terminate").click()
    page.get_by_text("AR Number").click()
    page.get_by_text("Area or Equipment").click()
    page.get_by_text("Condition or Practice").click()
    page.get_by_text("Event Number").click()
    page.get_by_text("Inspection Type").click()
    page.get_by_text("Last Contest Date").click()
    page.get_by_text("Mine Name").click()
    page.get_by_text("Modified Injury/Illness").click()
    page.get_by_text("Modified Likelihood").click()
    page.get_by_text("Modified Negligence").click()
    page.get_by_text("Modified Regulation").click()
    page.get_by_text("Modified_S&S").click()
    page.get_by_text("MSHA Case Number").click()
    page.get_by_text("MSHA Current Penalty").click()
    page.get_by_text("MSHA Final Order Date").click()
    
    page.get_by_role("button", name="Save").click()

    # Open “Columns” panel again 
    page.locator("text=Columns(").click()
    page.wait_for_selector("text=List of Columns Names")
    
    # Collect checked columns
    selected_columns = []
    checked_boxes = page.locator("input[type='checkbox'][checked]")

    count = checked_boxes.count()

    for i in range(count):
        checkbox_id = checked_boxes.nth(i).get_attribute("id")
        label_text = page.locator(f"label[for='{checkbox_id}']").inner_text()
        selected_columns.append(label_text)

     
    # Replace the columns name from selected_columns list because the in application, there is a missmatch in the column name in list & table header

    replacement_map = {
    'Citation Order No.': 'Citation/Order No.',
    'Action To Terminate': 'Action to Terminate',
    'Area or Equipment': 'Area',
    'Condition or Practice': 'Condition/Practice',
    'Modified Injury/Illness': 'Mod. Injury/Illness',
    'Modified Likelihood': 'Mod. Likelihood',
    'Modified Negligence': 'Mod. Negligence',
    'Modified Regulation': 'Mod. Regulation',
    'Modified_S&S': 'Mod. S&S',
    'Penalty Calculation': 'Penalty',
    'Penalty Calculation GFE': 'Penalty GFE'
    }
    
    final_selected_columns = [
    replacement_map.get(item, item)   # replace if exists, else keep original
    for item in selected_columns
    ]

    print("\nselected columns:")
    print(final_selected_columns)
    
    # Collect Visible Table Header Names
   
    page.wait_for_selector("thead th", timeout=60000)

    # Scroll to table (important)
    page.locator("thead").scroll_into_view_if_needed()
    page.mouse.wheel(0, 1000)

    # Try the most stable selector
    header_loc = page.locator("thead th div[class*='Content-Wrapper']")

    count = header_loc.count()
    headers = []

    for i in range(count):
        raw = header_loc.nth(i).inner_text().strip()
        clean = raw.split("\n")[0].strip()
        if clean:
            headers.append(clean)

    print("\nVisible Table Headers:")
    print(headers)
    

    # Compare Expected vs Visible Table Headers


    # Find missing columns
    missing_columns = [col for col in final_selected_columns if col not in headers]

    if missing_columns:
        raise AssertionError(
            f"❌ Test Failed!\n"
            f"The following expected columns are NOT visible in the table:\n"
            f"{missing_columns}\n\n"
            f"Expected (after replacement):\n{final_selected_columns}\n\n"
            f"Visible Headers:\n{headers}"
        )

    # If no mismatch
    print("\n✅ All selected columns are visible in the table.")
