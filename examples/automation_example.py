"""
Example: Automating a Form with selenium_web_automation_utils
"""
import time

from selenium.webdriver.common.by import By
from selenium_web_automation_utils.logging_utils import print_done
from selenium_web_automation_utils.selenium_utils import get_webdriver, find_element_wait, type_keys

firstname, lastname = "Roaming", "Saint"

# Open a web form and fill in fields
with get_webdriver() as driver:
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    # Find the input box for 'First name'
    first_name_input = find_element_wait(driver, By.XPATH, "//input[@name='fname']")
    current_firstname = first_name_input.get_attribute("value")  # Get current value
    print(f"Current Firstname: {current_firstname}")

    # Select the element and clear existing text
    first_name_input.click()
    first_name_input.clear()

    print(f"Changing Firstname to: {firstname}")
    type_keys(first_name_input, firstname)

    # Find the input box for 'Last name'
    last_name_input = find_element_wait(driver, By.XPATH, "//input[@name='lname']")
    current_lastname = last_name_input.get_attribute("value")  # Get current value
    print(f"Current Lastname: {current_lastname}")

    # Select the element and clear existing text
    last_name_input.click()
    last_name_input.clear()

    print(f"Changing Lastname to: {lastname}")
    type_keys(last_name_input, lastname)

    print_done("Form filled successfully!")
    time.sleep(3)