"""
Example: Web Scraping with selenium_web_automation_utils
"""
import time

from selenium.webdriver.common.by import By
from selenium_web_automation_utils.selenium_utils import get_webdriver, find_element_wait

# Open a website and extract the heading text
with get_webdriver() as driver:
    driver.get("https://www.example.com")

    # Find the first <h1> element
    heading = find_element_wait(driver, By.TAG_NAME, "h1")

    print(f"Page Heading: {heading.text}")
    time.sleep(2)
