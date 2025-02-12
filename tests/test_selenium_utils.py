from selenium.webdriver.common.by import By

from selenium_web_automation_utils.selenium_utils import (
    get_webdriver,
    find_element_wait,
    human_delay,
)


def test_get_webdriver():
    """Test if WebDriver initializes successfully."""
    with get_webdriver() as driver:
        assert driver is not None
        assert driver.capabilities is not None  # Check if driver started correctly

def test_find_element_wait():
    """Test if find_element_wait can locate an element."""
    with get_webdriver() as driver:
        driver.get("https://www.example.com")
        element = find_element_wait(driver, By.TAG_NAME, "h1", timeout=5)
        assert element is not None
        assert element.tag_name == "h1"

def test_human_delay():
    """Test human_delay function with random delay values."""
    import time
    start_time = time.time()
    human_delay(0.1, 0.2)
    end_time = time.time()
    assert 0.1 <= (end_time - start_time) <= 0.2
