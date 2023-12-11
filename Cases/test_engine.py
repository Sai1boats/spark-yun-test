import pytest
from playwright.sync_api import sync_playwright

from Pages.EnginePage import Engine
from Pages.LoginPage import Login


@pytest.fixture(scope='module')
def browser_init():
    browser=sync_playwright().start().chromium
    context = browser.launch(headless=False, slow_mo=50).new_context()
    return context

@pytest.fixture(scope='function')
def setUp(browser_init):
    page=browser_init.new_page()
    p=Engine(page)
    p.goto_homepage('http://127.0.0.1:9998')
    return p

class TestEnginePage:
    def test_show_add_engine_popup(self,setUp):
        page=setUp
        page.click_add_engine_button()
