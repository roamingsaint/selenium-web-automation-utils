"""
Example: Automating a Form with selenium_web_automation_utils
"""
from selenium.webdriver.common.by import By

from selenium_web_automation_utils.logging_utils import print_done
from selenium_web_automation_utils.selenium_utils import get_webdriver, find_element_wait, type_keys

firstname, lastname = "Roaming", "Saint"
# Open a web form and fill in fields
with get_webdriver() as driver:
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    # Find the input box for 'First name' and type into it
    first_name_input = find_element_wait(driver, By.XPATH, "//input[@name='fname']")
    print(f"Current Firstname: {first_name_input.text}")
    print(f"Changing Firstname to: {firstname}")
    type_keys(first_name_input, firstname)

    # Find the input box for 'Last name' and type into it
    last_name_input = find_element_wait(driver, By.XPATH, "//input[@name='lname']")
    print(f"Current Lastname: {last_name_input.text}")
    print(f"Changing Lastname to: {lastname}")
    type_keys(last_name_input, lastname)

    print_done("Form filled successfully!")
