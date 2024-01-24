import pytest
from selene import browser

from data.TestData import URLs


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = URLs.BASE_URL
    browser.config.window_height = 750
    browser.config.window_width = 1500
    yield
    browser.quit()
