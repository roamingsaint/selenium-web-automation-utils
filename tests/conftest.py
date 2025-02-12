import pytest
from selenium_web_automation_utils.selenium_utils import get_webdriver

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and yield a WebDriver instance."""
    with get_webdriver() as driver:
        yield driver  # Provide the WebDriver instance to the test
