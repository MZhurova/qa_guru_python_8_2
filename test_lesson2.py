from selene.support.shared import browser
from selene import be, have


def test_search(browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_not_found(browser_size):
    text = 'erwereqr322343j77ff'
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('[id="botstuff"]').should(have.text('ничего не найдено.'))
    print("\n")
    print("По заданному поиску " + text + " ничего не найдено")
