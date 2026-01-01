import re
import time
import random
from playwright.sync_api import Page, expect
from config import *
    
def test_login(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    expect(page.get_by_role("heading", name="Company Management")).to_be_visible()
    expect(page.get_by_role("button", name="Add Company")).to_be_visible()
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
    
    page.wait_for_load_state("domcontentloaded")
    expect(page.get_by_role("heading", name="IWT Analytics Platform")).to_be_visible()
    

def test_search_company(page: Page) -> None:
     # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()

    # Wait for dashboard to load
    page.wait_for_selector("text=Company Management", timeout=20000)

    # Search for company
    search_box = page.get_by_role("textbox", name="Search Company")
    search_box.fill("Barrick Nevada")

    # Wait for search results to appear
    page.wait_for_timeout(2000)  # small delay for results to render
    expect(page.get_by_text("Barrick Nevada Holding LLC")).to_be_visible(timeout=10000)

    # Logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
    

def test_add_company(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    #Open Add company form
    page.get_by_role("button", name="Add Company").click()
    page.get_by_role("textbox", name="SAP Account Id *").click()
    page.get_by_role("textbox", name="SAP Account Id *").fill("99890")
    page.get_by_role("textbox", name="MSHA Company Name *").click()
    page.get_by_role("textbox", name="MSHA Company Name *").fill("Steve  McGee")
    page.wait_for_timeout(3000)
    page.wait_for_selector("li:has-text('Steve  McGee')", state="visible", timeout=10000)
    page.get_by_text("Steve  McGee").click()
    
    # Address
    page.get_by_role("textbox", name="Address Line 1 *").fill("Washington U-street")
    page.locator("#stateId").select_option("1")
    page.get_by_label("City *").select_option("1")
    page.get_by_role("textbox", name="Zip/Postal Code *").fill("990978")
    page.get_by_role("textbox", name="Phone Number* Select Module").fill("9876567890")

    # Select Modules
    page.get_by_text("Location").click()
    page.get_by_text("Production").click()
    page.get_by_text("Atmosphere").click()
    page.get_by_role("dialog").get_by_text("Compliance").click()

    # Submit
    page.get_by_role("button", name="Add", exact=True).nth(1).click()

    # Verify success message and entry
    expect(page.get_by_text("Company Added successfully")).to_be_visible(timeout=10000)
    expect(page.get_by_text("Steve  McGee")).to_be_visible()

    # Logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()


def test_edit_company(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    page.get_by_role("row", name="99890 Steve McGee 0040469 USA").locator("#editCompany").click()
    page.get_by_role("textbox", name="Address Line 1 *").click()
    page.get_by_role("textbox", name="Address Line 1 *").fill("Washington U-street pune")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Company updated successfully")).to_be_visible()
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
    

def test_activate_deactivate_company(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    page.get_by_role("row", name="99890 Steve McGee 0040469 USA").locator("label div").click()
    expect(page.get_by_text("Company deactivated")).to_be_visible()
    page.get_by_title("Activate Company", exact=True).click()
    expect(page.get_by_text("Company activated successfully")).to_be_visible()
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()



def test_add_mine(page: Page) -> None:
    # Login
    # Go to login page
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    # Login
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    page.wait_for_selector("text=Company Management", timeout=20000)

    # Open Lafarge and click Add Mine
    page.get_by_text("Steve  McGee", exact=True).click()
    page.get_by_role("button", name="Add Mine").click()
    page.wait_for_selector("text=Add Mine", timeout=10000)

    # Fill MSHA Mine Name
    page.get_by_role("textbox", name="Enter MSHA Mine Name").fill("Pioneer")
    page.wait_for_selector("li:has-text('Pioneer Portable Crusher')", timeout=10000)
    page.get_by_text("Pioneer Portable Crusher").click()

    # Select Time Zone
    page.get_by_role("textbox", name="Select Time zone").fill("pac")
    page.wait_for_selector("li:has-text('Pacific/Chatham')", timeout=5000)
    page.get_by_text("Pacific/Chatham").click()

    # Adress, State & City
    page.get_by_role("textbox", name="Address Line 1 *").fill("Washington U-street")
    page.locator("[name='stateId']").scroll_into_view_if_needed()
    page.locator("[name='stateId']").select_option(index=1)

    page.locator("[name='cityId']").scroll_into_view_if_needed()
    page.locator("[name='cityId']").select_option(index=1)

    # Fill Zip Code
    page.get_by_role("textbox", name="Zip/Postal Code *").fill("98786")

    # Submit and confirm
    page.get_by_title("Click to add new mine").click()
    page.get_by_role("button", name="Yes").click()

    # Verify success
    expect(page.get_by_text("Mine created successfully")).to_be_visible(timeout=10000)
    
    # Logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
    

def test_edit_mine(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    # Wait for dashboard to load
    page.wait_for_selector("text=Company Management", timeout=20000)

    # Select company
    page.get_by_text("Steve McGee").click()

    # Click edit icon inside the company/mine table row
    page.get_by_title("Edit Mine").get_by_role("img").click()

    # Wait for edit dialog
    expect(page.get_by_title("Edit Mine")).to_be_visible(timeout=10000)

    # Click Save
    page.get_by_role("button", name="Save").click()

    # Verify success message
    expect(page.get_by_text("Mine updated successfully")).to_be_visible(timeout=10000)

    # Logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()


def test_activate_deactivate_mine(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    # Wait for dashboard to load
    page.wait_for_selector("text=Company Management", timeout=20000)

    # Select company
    page.get_by_text("Steve McGee").click()

    # operate toggle switch
    page.get_by_title("Deactivate Mine").click()
    expect(page.get_by_text("Mine deactivated successfully")).to_be_visible()
    page.get_by_title("Activate Mine").click()
    expect(page.get_by_text("Mine activated successfully")).to_be_visible()

    # Logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
    

def test_add_company_user(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    

    # Wait for dashboard to load
    page.wait_for_selector("text=Company Management", timeout=20000)

    # Click 'Add Company User' for Lafarge
    page.get_by_role("row", name="99890 Steve McGee 0040469 USA").locator("#addCompanyUser").click()
    

    # Fill user details
    page.get_by_role("textbox", name="Enter First Name").fill(Company_user_first_name)
    page.get_by_role("textbox", name="Enter Last Name").fill(Company_user_last_name)
    
    # Generate unique email ID using timestamp + random number
    unique_suffix = int(time.time())  # current timestamp
    random_num = random.randint(100, 999)  # extra randomness
    unique_email = f"test{unique_suffix}{random_num}@yopmail.com"
    
    
    page.get_by_role("textbox", name="Enter Email Address").fill(unique_email)
    page.get_by_role("textbox", name="Confirm Email Address").fill(unique_email)

    # Select role
    # page.locator("#role").select_option("697")   # or use visible text if known, e.g. select_option(label="Corp Admin")
    page.locator("#role").select_option(label="Corp Admin")   
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Add", exact=True).click()
    page.get_by_role("button", name="Add", exact=True).click()

    # Verify success message
    expect(page.get_by_text("User added successfully")).to_be_visible(timeout=10000)

    # logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()
  
  
def test_add_mine_user(page: Page) -> None:
    # Login
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
    page.get_by_role("textbox", name="Username").fill(USERNAME)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    
    # Wait for dashboard to load
    page.wait_for_selector("text=Company Management", timeout=20000)

    # Select company
    page.get_by_text("Steve McGee").click()

    # Click edit icon inside the company/mine table row
    page.get_by_role("row", name="Pioneer Portable Crusher 1700716").get_by_role("button").click()
    
    # Fill user details
    page.get_by_role("textbox", name="Enter First Name").fill(Mine_user_first_name)
    page.get_by_role("textbox", name="Enter Last Name").fill(Mine_user_last_name)
    
    # Generate unique email ID using timestamp + random number
    unique_suffix = int(time.time())  # current timestamp
    random_num = random.randint(100, 999)  # extra randomness
    unique_email = f"test{unique_suffix}{random_num}@yopmail.com"
    
    
    page.get_by_role("textbox", name="Enter Email Address").fill(unique_email)
    page.get_by_role("textbox", name="Confirm Email Address").fill(unique_email)

    # Select role
    page.locator("#role").select_option(label="Mine Admin")   
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Add", exact=True).click()
    page.get_by_role("button", name="Add", exact=True).click()


    # Verify success message
    expect(page.get_by_text("User added successfully")).to_be_visible(timeout=10000)

    # Optional logout
    page.get_by_text("IU").click()
    page.get_by_role("button", name="Logout").click()    



# def test_setting_user_operations(page: Page) -> None:
#     # Login
#     page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
#     page.get_by_role("textbox", name="Username").fill(USERNAME)
#     page.get_by_role("textbox", name="Password").fill(PASSWORD)
#     page.get_by_role("button", name="Sign In").click()
#     expect(page.get_by_role("heading", name="Company Management")).to_be_visible()
#     page.get_by_role("link", name="Settings").click()
#     page.get_by_text("Steve McGee").click()
    
#     # Activate/ Deactivate user
#     page.get_by_role("row", name = Company_user_first_name + " "+ Company_user_last_name).locator("label div").click()
#     expect(page.get_by_text("User deactivated successfully")).to_be_visible()
#     page.wait_for_timeout(2000)
#     page.get_by_role("row", name = Company_user_first_name + " "+ Company_user_last_name).get_by_role("cell").nth(3).click()
#     page.wait_for_timeout(2000)
#     expect(page.get_by_text("User activated successfully")).to_be_visible()

#     # Edit user
#     page.get_by_title("Edit User").nth(1).click()
#     page.get_by_role("button", name="Save").click()
#     expect(page.get_by_text("User updated successfully")).to_be_visible()

#     # Reset password
#     page.get_by_role("row", name= Company_user_first_name + " "+ Company_user_last_name).locator("path").nth(2).click()
#     page.get_by_role("button", name="Yes, Reset Password").click()
#     expect(page.get_by_text("Password reset successfully")).to_be_visible()
    
#     # Search user
#     page.get_by_role("textbox", name="Search User").click()
#     page.get_by_role("textbox", name="Search User").fill(Company_user_first_name + " "+ Company_user_last_name)
#     expect(page.get_by_role("cell", name= Company_user_first_name + " "+ Company_user_last_name)).to_be_visible()
#     page.get_by_role("textbox", name="Search User").click()
#     page.get_by_role("textbox", name="Search User").fill("")
#     expect(page.get_by_role("cell", name= Mine_user_first_name + " "+ Mine_user_last_name)).to_be_visible()
#     page.get_by_text("IU").click()
#     page.get_by_role("button", name="Logout").click()



# def test_delete_mine(page: Page) -> None:
#     # Login
#     page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
#     page.get_by_role("textbox", name="Username").fill(USERNAME)
#     page.get_by_role("textbox", name="Password").fill(PASSWORD)
#     page.get_by_role("button", name="Sign In").click()
    
#     page.get_by_text("Steve McGee").click()
#     page.get_by_title("Delete Mine").locator("path").click()
#     page.get_by_role("button", name="Delete").click()
#     expect(page.get_by_text("Mine deleted successfully")).to_be_visible()
#     page.get_by_text("IU").click()
#     page.get_by_role("button", name="Logout").click()

    



# def test_delete_company(page: Page) -> None:
#     # Login
#     page.goto(URL, wait_until="domcontentloaded", timeout=60000)  
#     page.get_by_role("textbox", name="Username").fill(USERNAME)
#     page.get_by_role("textbox", name="Password").fill(PASSWORD)
#     page.get_by_role("button", name="Sign In").click()

#     # Wait for dashboard to load
#     page.wait_for_selector("text=Company Management", timeout=20000)

#     # Delete the target company
#     page.get_by_role("row", name=re.compile(r"Steve McGee")).locator("#deleteCompany").click()
#     page.wait_for_selector("text=Delete Company", timeout=5000)
#     page.get_by_role("button", name="Delete", exact=True).click()

#     # Wait for success message or confirmation of deletion
#     expect(page.get_by_text("Company deleted successfully")).to_be_visible(timeout=10000)

#     # Logout from the application
#     page.get_by_text("IU").click()
#     page.get_by_role("button", name="Logout").click()
