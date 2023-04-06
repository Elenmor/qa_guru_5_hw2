import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_open():
    browser.open('https://google.com')
    browser.driver.set_window_size(1920, 1080)
    yield
    browser.quit()
def test_successful_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print ('Поиск усешен')

def test_unscessful_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('аааапыапрыавырдлашыа').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print ('Поиск не дал результатов')