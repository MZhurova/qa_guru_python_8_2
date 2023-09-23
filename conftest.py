import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_open():
    browser.open('https://google.com')


@pytest.fixture()
def browser_size():
    browser.config.window_width = 1400
    browser.config.window_height = 900

    yield

    browser.quit()
