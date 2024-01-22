import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.wait_for_no_overlap_found_by_js = True
    yield

    browser.quit()