import pytest
#from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def open():
     pass

     yield


     browser.open('https://google.com')





def test_search(open, cloce):
     pass
#     browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
 #    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

@pytest.fixture
def cloce():
     pass




