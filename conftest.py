import pytest
from selene import browser



@pytest.fixture(autouse=True)
def browser_open():
     browser.open('https://google.com')


@pytest.fixture()
def browser_size(browser_open):
     browser.driver.maximize_window()

     yield

     browser.quit()